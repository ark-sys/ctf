# CTF Writeups & Exploits

A personal archive of challenges solved across several CTF platforms, with
write-ups, exploit scripts, and supporting artifacts (scans, binaries,
captures, loot) kept alongside each challenge.

Most RootMe write-ups are in French and follow a **Description / Exploit**
format inside that challenge's own `README.md`.

## Layout

```
.
├── rootme/      RootMe challenges, grouped by category
├── tryHackMe/   TryHackMe rooms/boxes
├── kafctf/      kafCTF challenges
└── isticctf/    ISTIC CTF challenges
```

## RootMe

### App - Script (`rootme/app-script`)

| Challenge | Writeup |
|---|---|
| ch1 | [sudo - weak configuration](rootme/app-script/ch1/README.md) |
| ch7 | [Perl - Command injection](rootme/app-script/ch7/README.md) |
| ch8 | [Python - PyJail 1](rootme/app-script/ch8/README.md) |
| ch9 | [Python - PyJail 2](rootme/app-script/ch9/README.md) |
| ch10 | [Python - Jail - Exec](rootme/app-script/ch10/README.md) |
| ch11 | [Bash - System 1](rootme/app-script/ch11/README.md) |
| ch12 | [Bash - System 2](rootme/app-script/ch12/README.md) |
| ch13 | [PHP - Jail](rootme/app-script/ch13/README.md) |
| ch14 | [Bash - Restricted shells](rootme/app-script/ch14/README.md) |
| ch16 | [Bash - unquoted expression injection](rootme/app-script/ch16/README.md) |
| ch18 | [Powershell - Command Injection](rootme/app-script/ch18/README.md) |
| ch19 | [Powershell - SecureString](rootme/app-script/ch19/README.md) |
| ch20 | [Powershell - Basic jail](rootme/app-script/ch20/README.md) |
| ch21 | [notes](rootme/app-script/ch21/README.md) |
| ch23 | [LaTeX - Input](rootme/app-script/ch23/README.md) |
| ch24 | [LaTeX - Command execution](rootme/app-script/ch24/README.md) |
| SAH | [SSH - Agent Hijacking](rootme/app-script/SAH/README.md) |
| SOH | [Shared Objects hijacking](rootme/app-script/SOH/README.md) |
| python-pickle | [Python - pickle](rootme/app-script/python-pickle/README.md) |
| Docker-talk-through-me | [Docker socket escape](rootme/app-script/Docker-talk-through-me/README.md) |
| docker-sys-admin | exploit/loot only, no writeup |

### App - Système (`rootme/app-systeme`)

| Challenge | Writeup |
|---|---|
| ch72 | [PE32 - Stack buffer overflow basic](rootme/app-systeme/ch72/README.md) |
| ch13, ch14, ch35, ch45, ch45_s, ch65 | exploit/loot only, no writeup |

### Cracking (`rootme/cracking`)

| Challenge | Writeup |
|---|---|
| ch8 | [ELF x86 - CrackPass](rootme/cracking/ch8/README.md) |
| ch20 | [ELF x86 - No software breakpoints](rootme/cracking/ch20/README.md) |
| ch23 | [ELF ARM - Basic Crackme](rootme/cracking/ch23/README.md) |
| ch27 | [ELF MIPS - Basic Crackme](rootme/cracking/ch27/README.md) |
| ch9, ch19, ch32, ch36, + Ghidra project | binaries/scripts only, no writeup |

### Other categories

The following categories hold exploit scripts, scans, and loot files per
challenge, but no dedicated write-up yet:

- `rootme/crypto` — PIDencryption, ch03/04/05/07/10/11/20 crypt
- `rootme/forensic` — ch12/13/21 forensic
- `rootme/programming` — captchaprog, quickresp, suiteprog
- `rootme/realist` — ch1/6/7 realist
- `rootme/steganography` — ch9/10/11/13/14/15/16 steg, LSB-Steganography
- `rootme/web-client` — ch22client
- `rootme/web-server` — ch13/18/21/35/36/37/38/43/44/45/47/49/50/53/55/59/60/61 web
- `rootme/mrrobot`, `rootme/network`, `rootme/ctfalltheday` — Mr. Robot VM,
  network pcap/firewall challenge, CTF-all-the-day boxes (LAMPCTF5, SSRFBox)

## TryHackMe (`tryHackMe`)

Boxes/rooms with exploit scripts, fuzzers, scans, and loot (creds, hashes,
dumps). No dedicated write-ups yet:

- `exploit/` — daily-bugle, skynet, overpass2, relevant, internal, vulnversity
- `brainpan1`, `brainstorm`, `bufferoverflow` — binary exploitation / buffer
  overflow practice
- `gatekeeper` — Windows AD box (exploit, Firefox decrypt, loot)
- `attackingkerberos` — Kerberoasting / AS-REP roasting room

## kafCTF (`kafctf`)

- `web/` — web challenge scan
- `misc/` — 707Rainbows
- `pwn/` — SimpleAuthorize

## ISTIC CTF (`isticctf`)

- `steg/` — steganography challenge (LSB extraction, EXIF/metadata analysis)
