#encoding:utf8

#essencial caso sejam tres numeros diferente

def maximo(d,e,f):
	
	if d>e and d>f:
		return d
		
	elif e>d and e>f:
		return e

	else:
		return f
		
d=float(input("Insira o valor de d: "))
e=float(input("Insira o valor de e: "))
f=float(input("Insira o valor de f: "))

maximo=maximo(d,e,f)

print("O valor máximo entre {}, {} e {} é {}.".format(d,e,f,maximo))

#caso existam numeros iguais

def maximo(a,b,c):
	if a > b and a>c:
		return a
		
	elif b > a and b>c:
		return b
	
	elif c>a and c>b:
		return c
		
	elif c==a and c>b:
		return c
	
	elif c==b and c>a:
		return c
		
	elif a==b and a>c:
		return a
	
	else:
		return a
	
	
a=float(input("Insira o valor de a: "))
b=float(input("Insira o valor de b: "))
c=float(input("Insira o valor de c: "))

maximo=maximo(a,b,c)

print("O valor máximo entre {}, {} e {} é {}.".format(a,b,c,maximo))
	
