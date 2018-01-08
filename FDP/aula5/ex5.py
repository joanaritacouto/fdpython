def max2(x,y):

	if x>=y:
		maior=x
	else:
		maior=y
	return maior

def max3 (x,y,z):
	m= max2(x,y)
	if m>= z:
		print('Número maior: ', m)
	else:
		print('Número maior: ', z)
			

x = float(input('primeiro número: '))
y = float(input('segundo número: '))
z = float(input('terceiro númeor: '))

max3(x,y,z)


		
