from PIL import Image, ImageDraw
import sys
im = Image.open("qrcode2.png")

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
im.save("qrcode2.png", "PNG")
