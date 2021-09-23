#!/usr/bin/python
# -*- coding: UTF-8 -*-

import string

with open("ch7.bin","rb") as file:
	data = file.read()


res=""
for i in data:
	res+=chr(ord(i)-10)
print res




