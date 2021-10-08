#!/bin/python3 env
from PIL import Image, ImageDraw
import sys


with open("data","r") as file:
	data = file.readlines()
#data=data.replace('\n','')
pixels=[]
for i in data:
	temp = i.split("+")
	length=0
	for y in temp:
		if y[:1] == '0':
			for z in range(int(y[2:])):
				length+=1
				pixels.append((255,255,255))
				if length==100:
					break
		else:
			for z in range(int(y[2:])):
				length+=1
				pixels.append((0,0,0))


image_out = Image.new("RGB", (100, len(data)), "white")
image_out.putdata(pixels)
image_out.save("res.png","PNG")
