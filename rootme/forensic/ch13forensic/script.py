import string
import base64
import binascii

print "Opening file ..."
with open("data.txt","r") as file:
	data = file.readlines()



res=[]
time=[]

print "Splitting..."
for i in data:
	if("order" in i):		
		res.append(i.split("&order=")[1].split(" ")[0].replace("%3D","="))
		time.append(i.split("[")[1].split("]")[0])
		
datadecoded=""
stringres=""
stringtab=[]
bindata=""
count=0
print "Decoding..."
for i in range(0,len(res)):
	if((int(time[i][18:-6])-int(time[i-1][18:-6]))%60)==0:
		if count==3:
			count=0
			stringres+=" "
		else:
			stringres+="00"
			count+=1
	if((int(time[i][18:-6])-int(time[i-1][18:-6]))%60)==2:
		if count==3:
			stringres+="0"
			stringtab.append(stringres)
			bindata+=stringres
			bindata+=" "
			stringres=""
			count=0
		else:
			stringres+="01"
			count+=1	
	if((int(time[i][18:-6])-int(time[i-1][18:-6]))%60)==4:
		if count==3:
			stringres+="1"
			stringtab.append(stringres)
			bindata+=stringres
			bindata+=" "
			stringres=""
			count=0
		else:
			stringres+="10"
			count+=1
	if((int(time[i][18:-6])-int(time[i-1][18:-6]))%60)==6:
		if count==3:
			count=0
			stringres+=" "
		else:
			stringres+="11"
			count+=1
	
	datadecoded+=("Request n.%d at %s\n"+base64.b64decode(res[i])+'\n\n')%(i,time[i])
print "Data saved to output..." 


lol1=""
lol2=""
for i in range(0,len(stringtab)):
	if " " in stringtab[i]:
		lol1=stringtab[i].split(" ")[0]
		lol2=stringtab[i].split(" ")[1]
		stringtab[i]=lol1
		stringtab.insert(i+1,lol2)

for i in range(0,len(stringtab)):	
	while(len(stringtab[i])%8!=0):
		stringtab[i]="0"+stringtab[i]
resoutput=""
for i in stringtab:
	resoutput+=binascii.unhexlify("%x"%int(i,2))		

print "Flag is %s"%resoutput
with open("output","w") as f:
	f.write(datadecoded)

print "Done..."
