# Bash - System 1

# Description : 

> Le programme applique les ID utilisateur réels et effectifs du processus actuel à **app-script-ch11-cracked** (qui est aussi l'utilisateur capable de lire le fichier **.passwd**).
> Le programme exécute ensuite la commande `ls` sur le fichier **.passwd**.

# Exploit : 

> Il est donc possible d'exploiter l'exécution de la commande `ls` en la faisant pointer sur la commande `cat` à la place.
> 
> Pour ce faire, il faut créer un nouveau dossier dans **/tmp**.
> 
> `mkdir -p /tmp/ch11-exploit`
> 
> Ensuite, il faut créer un lien symbolique vers la commande `cat` dans le nouveau répertoire, en renommant ce lien `ls`.
> 
> `ln -s /bin/cat /tmp/ch11-exploit/ls`
> 
> Et enfin, il faut exporter le nouveau chemin dans la variable d'environnement *PATH*, afin que le lien symbolique puisse s'exécuter avant les programmes de base situés dans le répertoire **/usr/bin**.
> 
> `export PATH=/tmp/ch11-exploit`
> 
> Maintenant, il suffit de lancer le programme `./ch11` qui affichera le flag suivant : **!oPe96a/.s8d5**