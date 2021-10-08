with open("data","r") as file:
	data = file.readlines()
output=[]
string=""
word=1
line=1
for lines in data:
	temp = lines.replace('\n',' ')
	for char in temp:
		if char == ' ' or char == '\'':
			word+=1
			string+=' '
		else:	
			print "old char '%s' n. is %d, new char '%s' n is %d"%(char,ord(char),chr(ord(char)+word),ord(char)+word)
			index = ord(char)+word
			string+=chr(index)
	string+=' '
	output.append(string)
	string=""
start=""
end=""

restext=""
for i in output:
	start+=i[:1]
	end+=i[-2:-1]
	restext+=i+'\n'
password=start+end
print restext
print
print "Flag is : %s"%password