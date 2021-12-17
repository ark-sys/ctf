# Bash - unquoted expression injection

# Description : 

> Comme son titre l'indique, ce défi consiste à exploiter des expressions qui ne sont pas correctement entourées de guillemets dans un script bash.
>
> Plus précisément, à la ligne 12 du script, il y a un test entre le contenu de la variable **$PASS** et le contenu de la variable **$1** (entrée utilisateur). Si le test est positif, le flag s'affiche à l'écran.

# Exploit : 

> Il est donc nécessaire de rendre positif le test de la ligne 12, et pour cela il suffit de fournir en entrée l'expression suivante : 
> 
> **"1 -o 1 -eq 1"**
>
> De cette façon, même si la première partie de l'expression lors du test est négative, la deuxième partie, précédée de **-o** (ou), rendra le résultat positif et fournira ainsi le flag suivant : **8246320937403**