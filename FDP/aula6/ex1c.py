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

def somalista():
	soma=0
	l=listanum()
	print (l)
	for i in l:
		soma=soma+i
		
	print (soma)	
	return soma	
	

somalista()	