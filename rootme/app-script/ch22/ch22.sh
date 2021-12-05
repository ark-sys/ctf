#!/bin/bash
 
# Let's learn some bash tips and tricks!  Yeah!
 
PATH=$(/usr/bin/getconf PATH || /bin/kill $$)
 
lockfile="/tmp/app-script_ch22.lock"
exec 9>"$lockfile"
if ! flock -n 9
then    printf 'Only one running instance is allowed.\n';
        exit 1
fi
 
# See, you can pass a non-integer value to sleep!
sleep 0.314159265
 
# Create a temporary directory to avoid collision.
unset tmp TMPDIR
tmp="/tmp/$PPID/$$"
 
if [[ "$1" = "cleanup" ]] || [[ -e "$tmp" ]]
then  rm -rvf "$tmp"
      exit 1
fi
 
mkdir -p -m777 "${tmp}"
 
temp_dir=$(mktemp -d -p "$tmp" -u)
mkdir -m=777 "$temp_dir" || exit 1
 
# Let's cleanup the previous mess.
# (by the way, always quote your variables.  Always.  ALWAYS!)
trap 'rm -rf "$tmp"; rm -f "$lockfile"' EXIT TERM INT
 
# How to make a awk(1) + ~grep(1) in the very same command?
v=$(awk '/pattern/{print $1}' <<< "$(ps ax)")
if [ "$v" = "foo" ]
then printf 'Wut?!\n'
fi
 
# You can use the {1..n} builtin instead of seq(1).
for i in {95..100}
do
    # echo(1) sucks.  Use printf(1) instead.
    printf '%d\n' "$i" > "$temp_dir"/file."$i"
done
 
# With find(1) you can specify the size of a file you are looking for, thanks to
# the -size option.  In the next command, "-size 4c" matches 4-bytes files.
 
# Using + instead of \; is often more efficient, because we do not spawn a
# process per matched file.
find "$temp_dir" -type f -size 4c -exec cat {} +
 
# Cleanup the mess.  Use -print0 + xargs -0 to avoid separator tricks
find "$temp_dir" -type f -print0 | xargs -0 rm
 
# That's all for now, folks.

