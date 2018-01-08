import math


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
	
def maximo(l):
	max=-math.inf
	
	for i in l:
		if i>max:
			max=i	

	return max


def metademaximo():
	l=listanum()
	max = maximo(l)
	numeros=0

	max = float(max)

	mm=max/2

	for i in l:
		if i<mm:
			numeros=numeros+1

	print(numeros)
		
metademaximo()