# nome:Joana Rita Linhares Couto Nmec:88954

print('Calculadora da taxa de alcoolémia')

def menu():
	print('0 - sair')
	print('1 - introduzir nova média')
	print('2 - mostrar média atual')

	while true:
		op= input('Opção? ')

		if op == '0':
			print('FIM! Até breve!')
			break

		elif op == '1':
			lerValorRealPositivo(n)


		elif op == '2':
			taxa(p,a)

		else:
			print('Opção inválida')	

def lerValorRealPositivo(p,a):
	p= float(input('Peso (Kg)? '))
	a= float(input('álcool ingerido (g)? '))

	if p != float:
		print ('Erro')
		p= float(input('Peso (Kg)? '))	

	return p

	if a!= float:
		print ('Erro')
		a= float(input('Peso (Kg)? '))
	
	return a
	taxa(p,a)	


def taxa(p,a):
	p= float(input('peso (Kg)? '))
	a= float(input('álcool ingerido (g)? '))	

	TAXA=a/(p*1.1)
	return TAXA

	print('taxa de alcoolémia: ', taxa(p,a))


t= taxa(p,a)

def informaçao(t):
	if t<0.5:
			print('O condutor pode conduzir')

	elif 0.5<=t<=1.2:
			print('O condutor comete uma contraordenação')

	elif t>1.2:
			print('O condutor comete um crime')

informaçao(t)	



	






