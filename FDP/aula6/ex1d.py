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

def contagemlista():
	l=listanum()
	print (l)

	n= int(input('valor desejado: '))

	somainf=0

	for i in l:
		if n>i:
			somainf=somainf+1
				
	return somainf
	
print(contagemlista())