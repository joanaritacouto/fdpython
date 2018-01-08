def listanum():
	lista=[]
	
	while True :
		x= input('Número? ')

		if len(x) == 0:
			break

		else:	
			x= float(x)	

		lista.append(x)	


	return lista 
	
def maximo():
	import math
	max=-math.inf
	l=listanum()

	for i in l:
		if i>max:
			max=i

	print ('máximo', max)
			 	
maximo()			 	
