#Escreva um programa que dada uma data composta pelo mês e ano (valores inteiros introduzidos através do teclado), calcula e escreve no terminal o número de dias desse mês.
#Um ano é bissexto se for múltiplo de 4, com exceção dos fins de século, (múltiplos de 100), que só são bissextos se forem múltiplos de 400. 

def bissexto(a):
	if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
		return True
	else:
		return False

def diasdomes(m, a):
	dias= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	ndias= dias [m]
	if m == 2 and bissexto(a):
		ndias= 29
	return ndias

a= int( input('Ano: '))
m= int( input('Mês: '))
d= diasdomes(m, a)
print( 'O mês ', m, 'do ano ', a, 'tem ', d, 'dias.')
