#encoding:utf8

def maximo(a,b):
	if a > b:
		return a
	elif b > a:
		return b
		
	else: 
		return a
		
a=float(input("Insira o valor de a: "))
b=float(input("Insira o valor de b: "))
		
maximo=maximo(a,b)

print("O valor máximo entre {} e {} é {}.".format(a,b,maximo))
	
		
