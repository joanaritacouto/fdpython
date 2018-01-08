tel=[938555182,234567111,776882333]
nome=['Angelina','Brad', 'Claudia']

def ListadeCont(tel,nome):
	name = input('Nome?')

	cont = 0

	for i in nome:
		if i == name:
			name= tel[cont]
			print (name)
			break
		cont += 1

ListadeCont(tel,nome)