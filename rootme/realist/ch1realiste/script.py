import requests
import base64
url="http://challenge01.root-me.org/realiste/ch1/login.php"
pass2="YXplcnR5NjU0JiY="
pass2=base64.b64decode(pass2)



s = requests.session()

res = s.post(url, params={'login':'admin','pass2':pass2,'mess':'Se+connecter','dec':''})

print res.text