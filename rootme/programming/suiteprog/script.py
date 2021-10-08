import requests
import base64
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import operator

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
def solveeq(u0, unn, i1, i2, op1, op2, op3):
	un = u0
	n = 0 
	block1=0
	block2=0
	while(n<unn):
		block1 = ops[op1](i1,un)
		block2 = ops[op3](n,i2)
		res = ops[op2](block1,block2)
		un=res
		n+=1
	return res

url = 'http://challenge01.root-me.org/programmation/ch1/'
r = requests.Session()
stuff = r.get(url)
soup = BeautifulSoup(stuff.content,'html.parser')

res = soup.find("body")

Unp = res.text.split('U0')[0]
U0 = res.text.split('U0')[1].split('= ')[1].split('Y')[0]
Unn = res.text.split('find U')[1].split('Y')[0]
print(Unp)
print('U0 = %s'%U0)
print('To %s'%Unn)

u0 = int(U0)
unn = int(Unn)
eq = Unp.split(' ')
i1 = int(eq[3])
i2 = int(eq[-2])
op1 = eq[4]
op2 = eq[7]
op3 = eq[10]

result = solveeq(u0, unn, i1, i2, op1, op2, op3)
print('result is %s'%str(result))
link = 'http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result='+str(result)
trylink = r.get(link)
print(trylink.content)
