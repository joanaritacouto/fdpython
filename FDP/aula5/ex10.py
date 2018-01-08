def sumall(a,b):
	soma=0
	for i in range(a,b+1):
		soma=soma+i
	return soma

a= int(input('primeiro número inteiro: '))
b= int(input('segundo número inteiro: '))		

sumall(a,b)
print ('soma de todos os elemetos entre {} e {} é igual a {}'.format(a,b, sumall(a,b)))
