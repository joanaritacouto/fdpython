#encoding:utf8

def soma(N):
	somaa=0
	for i in range(N):
		n=float(input("Insira o valor que quer somar: "))
		somaa=somaa+n
	return somaa

N=int(input("Insira quantos valores quer somar: "))
print(soma(N))

#ou 


def soma():
	somaa=0
	n=int(input("Insira um digito: "))
	while n != 0:
		somaa=somaa+n
		n=int(input("Insira um digito: "))
	return somaa
	
print(soma())
		

