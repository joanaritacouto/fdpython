def Leibniz(n):
	soma=0
	for i in range (n+1):
		conta= ((-1)**i)/(2*i+1)
		soma=soma+conta
	return soma

n=int(input('número de termos: '))

Leibniz(n)	 

print('para o {} termos, a soma é igual a {}'.format(n,Leibniz(n)))	