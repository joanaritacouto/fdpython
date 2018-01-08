
def algarismos(n):
	c=0
	for i in str (n):
		c=c+1
	return c


	
n=int(input('número inteiro positivo: '))

algarismos(n)	
print ('numero de algaritmos: ',algarismos(n))
