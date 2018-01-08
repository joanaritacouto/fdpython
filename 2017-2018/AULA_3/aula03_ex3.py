#encoding:utf8


#caso os numeros sejam os tres diferentes
a=float(input("Insira o valor do primeiro numero: "))
b=float(input("Insira o valor do segundo numero: "))
c=float(input("Insira o valor do segundo numero: "))

if a>b and a>c:
	print("O maior numero é", a)
elif b>a and b>c:
	print("O maior numero é", b)
else:
	print("O maior numero é", c)
	

#caso existam numeros iguais


a=float(input("Insira o valor do primeiro numero: "))
b=float(input("Insira o valor do segundo numero: "))
c=float(input("Insira o valor do segundo numero: "))

if a>b and a>c:
	print("O maior numero é", a)
elif b>a and b>c:
	print("O maior numero é", b)
elif c>a and c>b:
	print("O maior numero é", c)
		
elif c==a and c>b:
	print("O maior numero é", c)
	
elif c==b and c>a:
	print("O maior numero é", c)
		
elif a==b and a>c:
	print("O maior numero é", a)
	
else:
	print("O maior numero é", c)
	

	
