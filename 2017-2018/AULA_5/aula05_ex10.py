# encoding:utf8

def soma(a,b):
	if b>a:
		soma=a
		while b > a:
			soma=soma+b
			b=b-1
	elif a>b:
		soma=b
		while a>b:
			soma=soma+a
			a=a-1
	else:
		soma=a
	return soma
	
a=int(input("Insira o valor de a: "))
b=int(input("Insira o valor de b: "))
soma=soma(a,b)
print("A soma dos números entre {} e {} incluvisé é {}.".format(a,b,soma))
