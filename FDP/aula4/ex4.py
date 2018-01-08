x = int (input ('Número inteiro: '))
soma=0

for i in range(1,x):
	if x%i==0:
	 print('Divisor de {}: '.format(x), i)
	 soma=soma+i

if soma < x:
	print('Número Deficiente')
elif soma == x:
	print('Número Perfeito')
elif soma > x:
	print('Número Abundante')






