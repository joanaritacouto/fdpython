#encoding:utf8

n=int(input("Insira um número inteiro positivo: "))
soma=0

for i in range(1,n):
	if n%i==0:
		print(i)
		soma=soma+i
if n>soma:
	print("Número deficiente!")
elif n<soma:
	print("Número abundante!")
else:
	print("Numero perfeito!")

	
		
