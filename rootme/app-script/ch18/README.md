# Powershell - Command Injection

# Description :

> Ce challenge demande à l'utilisateur de rentrer le nom d'une table dans la base de données à afficher.
> Comme suggéré sur la page du défi, il s'agit donc d'une vulnérabilité liée à la commande Invoke-Expression.

# Exploit : 

> Il suffit d'ajouter un point-virgule au début de l'entrée pour concaténer une autre commande à exécuter. Dans ce cas, l'autre commande à exécuter est `cat .passwd`.
> 
> Le flag trouvé est : **SecureIEXpassword**