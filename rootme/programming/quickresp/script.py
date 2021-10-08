import requests
import base64
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image, ImageOps, ImageEnhance, ImageDraw
import pyqrcode
from pyzbar import pyzbar
import cv2

def qrcoderepair():
	im = Image.open("qrcode.png")

	draw = ImageDraw.Draw(im)
	draw.rectangle([18,18,81,81],"black")
	draw.rectangle([27,27,72,72],"white")
	draw.rectangle([36,36,63,63],"black")

	draw.rectangle([18,219,81,281],"black")
	draw.rectangle([27,228,72,272],"white")
	draw.rectangle([36,237,63,263],"black")

	draw.rectangle([219,18,281,81],"black")
	draw.rectangle([228,27,272,72],"white")
	draw.rectangle([237,36,263,63],"black")
	im.save("qrcode.png", "PNG")


url = 'http://challenge01.root-me.org/programmation/ch7/'
r = requests.Session()
stuff = r.get(url)
soup = BeautifulSoup(stuff.content,'html.parser')


res = soup.find("img")
data = res.get("src")
im = Image.open(BytesIO(base64.b64decode(data.split(',')[1])))
im.save('qrcode.png', 'PNG')

qrcoderepair()


im2 = cv2.imread("qrcode.png")
#results = scanner.scan(im2)
output = pyzbar.decode(im2)[0].data.split("is ")[1]
print(output)
response = {'metu': output}
out = r.post(url, data = response)
print(out.content)
soup2 = BeautifulSoup(out.content,'html.parser')
outres = soup2.find("p")
print
print(outres.text)
