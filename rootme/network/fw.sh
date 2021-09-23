#!/bin/sh
# author: absent minded admin

# iptables/ip6tables wrappers (see below)
IP4T() { :; }
IP6T() { :; }
IP46T() {
    IP4T "$@"
    IP6T "$@"
}

usage() {
    cat <<EOT

Usage:
    ${0##*/} {-h|--help}
    ${0##*/} [-v] -4     Reinitialize IPv4 firewall ruleset
    ${0##*/} [-v] -6     Reinitialize IPv6 firewall ruleset
    ${0##*/} [-v] -46    Reinitialize both IPv4&IPv6 firewall rulesets

Options:
    -v|--verbose            Print what's being done

EOT
}

verbose=false
do_IPv4=false
do_IPv6=false
[ $# -eq 0 ] && set -- '--help'
while [ $# -gt 0 ]; do
    case "$1" in
        -h|--help)      usage; exit 0;;
        -v|--verbose)   verbose=true;;
        -4)             do_IPv4=true;;
        -6)             do_IPv6=true;;
        -46|-64)    set -- "$@" -4 -6 ;;
        *)          echo "'$1': unknown option" >&2
                    usage >&2
                    exit 1
                    ;;
    esac
    shift
done

$do_IPv4 && IP4T() { $verbose && echo "IP4T $*"; /sbin/iptables "$@" ; }
$do_IPv6 && IP6T() { $verbose && echo "IP6T $*"; /sbin/ip6tables "$@" ; }

# --------------------------
# | filter: general policy |
# --------------------------
IP46T -P INPUT DROP
IP46T -P OUTPUT ACCEPT

# -------------------------------
# | reset the current rulesets: |
# -------------------------------
#    1) empty chains,
#    2) delete user-defined chains,
#    3) reset counters
for table in raw mangle filter nat; do
    IP46T -t $table -F
    IP46T -t $table -X
    IP46T -t $table -Z
done 2>/dev/null

# Create a chain we will jump to when we want to explicitely LOG & REJECT trafic
IP46T -N INPUT-FINAL
IP46T -A INPUT-FINAL -m limit --limit 2/sec --limit-burst 2 -j LOG --log-prefix 'FW_INPUT_DROP '
IP46T -A INPUT-FINAL -p tcp -j REJECT --reject-with tcp-reset
IP46T -A INPUT-FINAL -j REJECT

# Disable processing of any RH0 packet
# Which could allow a ping-pong of packets (TODO: other dangerous headers?)
IP6T  -A INPUT   -m rt --rt-type 0 -j DROP

# Drop INVALID packets ASAP, this will save some resources and
# they'll eventually be dropped by the kernel anyway
IP46T  -A INPUT   -m conntrack --ctstate INVALID -j DROP

# Don't filter anything from the loopback interface
IP46T -A INPUT  -i lo -j ACCEPT
# accept paquets from established 'connection' (in the sense of netfilter)
IP46T -A INPUT  -m conntrack --ctstate ESTABLISHED -j ACCEPT

# very basic ICMP handling
IP46T -N INPUT-ICMP
IP4T  -A INPUT-ICMP -p icmp -m conntrack --ctstate RELATED -j ACCEPT
IP4T  -A INPUT-ICMP -p icmp --icmp-type echo-request -j ACCEPT
# TODO: follow rfc4890
IP6T  -A INPUT-ICMP -p icmpv6 -m conntrack --ctstate RELATED -j ACCEPT
IP6T  -A INPUT-ICMP -p icmpv6 --icmpv6-type echo-request -j ACCEPT
IP6T  -A INPUT-ICMP -p icmpv6 --icmpv6-type router-advertisement -j ACCEPT
IP6T  -A INPUT-ICMP -p icmpv6 --icmpv6-type neighbour-advertisement -j ACCEPT
IP6T  -A INPUT-ICMP -p icmpv6 --icmpv6-type neighbour-solicitation -j ACCEPT

# LOG and REJECT other icmp packets
IP46T -A INPUT-ICMP -j INPUT-FINAL

# use the newly created chain!
IP4T  -A INPUT -p icmp -j INPUT-ICMP
IP6T  -A INPUT -p icmpv6 -j INPUT-ICMP

# accept ssh connections!
IP46T -A INPUT -p tcp --dport 22 -j ACCEPT


# Our web servers are regularly attacked: let's try to protect them
# check TCP flags (drop attack attempt)
IP46T -N CHK-TCP-FLAGS
IP46T -A CHK-TCP-FLAGS -p tcp --tcp-flags ALL FIN,URG,PSH         -j DROP
IP46T -A CHK-TCP-FLAGS -p tcp --tcp-flags ALL SYN,RST,ACK,FIN,URG -j DROP
IP46T -A CHK-TCP-FLAGS -p tcp --tcp-flags ALL ALL                 -j DROP
IP46T -A CHK-TCP-FLAGS -p tcp --tcp-flags ALL FIN                 -j DROP
IP46T -A CHK-TCP-FLAGS -p tcp --tcp-flags SYN,RST SYN,RST         -j DROP
IP46T -A CHK-TCP-FLAGS -p tcp --tcp-flags SYN,FIN SYN,FIN         -j DROP
IP46T -A CHK-TCP-FLAGS -p tcp --tcp-flags ALL NONE                -j DROP

# whitelist our clients
IP46T -N CHK-WHITELIST
IP46T -A CHK-WHITELIST -s example.net -j ACCEPT
IP46T -A CHK-WHITELIST -s fdlp.asdfnsec.com -j ACCEPT
IP46T -A CHK-WHITELIST -s pqr.naer-biz.lu -j ACCEPT

# chain to handle incomming HTTP trafic
IP46T -N INPUT-HTTP
# traffic to port 80 coming from our reverse proxy needs no further protection
IP46T -A INPUT-HTTP -s rp.root-me.org -p tcp --dport 80 -j ACCEPT
# check TCP Flags
IP46T -A INPUT-HTTP -j CHK-TCP-FLAGS
# Be extra-cautious with http://challenge01.root-me.org:54017/:
# restrict access with a whitelist
IP46T -A INPUT-HTTP -p tcp --dport 54017 -j CHK-WHITELIST
# apply some flood protection against remaining trafic
IP46T -A INPUT-HTTP -m limit --limit 3/sec --limit-burst 20 -j LOG --log-prefix 'FW_FLOODER '
IP46T -A INPUT-HTTP -m limit --limit 3/sec --limit-burst 20 -j DROP
# Previous rules ensure we're dealing with legitimate requests -> ACCEPT them now
IP46T -A INPUT-HTTP -j ACCEPT

# Enable the security on http-80 and http-54017 incomming http trafic:
IP46T -A INPUT -p tcp -m multiport --dports 80,54017 -j INPUT-HTTP


# LOG & REJECT everything else
IP46T -A INPUT -j INPUT-FINAL

