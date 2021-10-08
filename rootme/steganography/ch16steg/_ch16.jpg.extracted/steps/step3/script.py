import string
import binascii
with open("cipher", "r") as file:
	data = file.read()

def toString(binaryString):
    return "".join([chr(int(binaryString[i:i+8],2)) for i in range(0,len(binaryString),8)])

res=""



for i in data:
	if i.isupper():
		res+="0"
	if i.islower():
		res+="1"


data2 = toString(res)
print("res string is: %s"%res)
print(data2)
