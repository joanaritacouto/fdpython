def listanum():
	lista=[]
	
	while True :
		x= input('Número? ')

		if len(x) == 0:
			break

		else:	
			x= float(x)	

		lista.append(x)
		
	print (lista)
	return lista

listanum()	