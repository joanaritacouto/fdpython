#encoding:utf8

def digitos(N):
	c=0
	for i in str(N):
		c=c+1
	return c
	
N=int(input("Insira um número que quer testar: "))
print("O número {} possui {} digitos.".format(N,digitos(N)))

