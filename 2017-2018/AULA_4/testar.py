"""
for i in range(10):
	print("Aveiro")
	print(i)  #o 10 não é atingido
	
"""

"""
for i in range (10,2,-2):
	print(i)
"""

#numeros primos entre 10 e 20

for num in range(10,20):
	c=0
	for i in range(1,num+1):
		if num%i==0:
			c=c+1
	if c==2:
		print(num,"é primo")
	
