# nome:Joana Rita Linhares Couto Nmec:88954

p= float(input('peso (Kg)? '))
a= float(input('álcool ingerido (g)? '))

taxa=a/(p*1.1)

if taxa<0.5:
	print('taxa de alcoolémia de {}'.format(taxa))
	print('O condutor pode conduzir')

elif 0.5<=taxa<=1.2:
	print('taxa de alcoolémia de {}'.format(taxa))
	print('O condutor comete uma contraordenação')

elif taxa>1.2:
	print('taxa de alcoolémia de {}'.format(taxa))
	print('O condutor comete um crime')
		