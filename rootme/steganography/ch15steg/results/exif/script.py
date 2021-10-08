#import os
#import string


with open("comment","r")as f:
	data=f.readlines()
tab = [0,0,0,0,0,0,0,0,0,0]
res1=''
res2=''
for i in data:
	
	tab[len(i)-1]+=1
	if(len(i)-1==4):
		res1+=i
	if(len(i)-1==8):
		res2+=i
		
with open("output1","w") as output1:
	output1.write(res1)
with open("output2","w") as output2:
	output2.write(res2)
