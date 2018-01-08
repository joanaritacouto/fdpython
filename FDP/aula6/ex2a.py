tel=['938555182','234567111','776882333']
nome=['Angelina','Brad', 'Claudia']

def chamada(tel, nome):
	num = input('Número?')

	cont = 0
	for i in tel:
		if i == num:
			num = nome[cont]
			break
		cont += 1

	print(num)
	
chamada(tel,nome)
