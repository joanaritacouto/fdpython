#encoding:utf8

def Leibniz(n):
	soma=0
	for i in range(n+1):
		conta=((-1)**i)/(2*i+1)
		soma=soma+conta
	return soma
	
n=int(input("Insira o número de termos: "))
print(Leibniz(n))
