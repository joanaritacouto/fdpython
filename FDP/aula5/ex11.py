def soma(N):
	somaa=0
	for i in range(N):
		x= float(input('número: '))
		somaa=somaa+x
	return somaa
 
N= int (input('número de valores desejados: '))


print('a soma de todos os {} valores é igual a {}'.format(N, soma(N)))