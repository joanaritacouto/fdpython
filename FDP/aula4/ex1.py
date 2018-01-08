
total = 0
soma = 0.0
maior = None
menor = None

while True :
	n = float ( input ('número: '))

	if n==0 : 
		break

	total += 1
	soma = soma + n

	if maior == None or n > maior:
		maior = n

	if menor == None or n < menor:
		menor = n

media = soma / total

print()
print('Resultados')
print('----------------')
print('número de elementos: ' , total)
print('soma: ' , soma)
print('media: ' , media)
print('maior: ' ,  maior)
print('menor: ', menor) 		