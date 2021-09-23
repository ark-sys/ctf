import string
with open("data", "r") as file:
	data = file.readlines()

output=""
for lines in data:
	for char in lines:
		 if char.isalpha():
		 	output += chr(ord(char)+13)
		 else:
		 	output+=char

print output