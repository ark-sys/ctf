import requests
import base64
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image, ImageOps, ImageEnhance

url = 'http://challenge01.root-me.org/programmation/ch8/'
r = requests.Session()
stuff = r.get(url)
soup = BeautifulSoup(stuff.content,'html.parser')


res = soup.find("img")
data = res.get("src")
im = Image.open(BytesIO(base64.b64decode(data.split(',')[1])))
im.save('captcha.png', 'PNG')

output = pytesseract.image_to_string(Image.open('captcha.png'))
print(output)
response = {'cametu': output}
out = r.post(url, data = response)
print(out.content)
soup2 = BeautifulSoup(out.content,'html.parser')
outres = soup.get("p")
print(outres)
