
#encoding: utf8

def MDC(a, b):
	r = a%b
	if r !=0:
		return MDC(b,r)
	else:
		return b

a=int(input("Insira o primeiro valor: "))
b=int(input("Insira o segundo valor: "))
MDC=MDC(a,b)
print("O MDC entre {} e {} é {}.".format(a,b,MDC))

