#Adaptando o programa anterior de modo a pedir ao utilizador uma data composta pelo dia, mês, ano. Depois o programa deve determinar e imprimir a data do dia anterior e seguinte.
def diaanterior(d, m, a):
	da= d - 1
	ma= m
	aa= a
	
	if da == 0:
		da= 31
		ma= m - 1
		if ma == 0:
			ma= 12
			aa= a - 1
	return da, ma, aa

def bissexto(a):
	if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
		return True
	else:
		return False

def diaseguinte(d, m, a):
	ds= d + 1
	ms= m 
	ad= a
	
	if ds == 32 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12 ):
		ds= 1
		ms= m + 1
		if ms == 13:
			ms= 1
			ad= a + 1
	elif ds == 31 and (m == 4 or m == 6 or m == 9 or m == 11 ):
		ds= 1
		ms= m + 1
	elif ds == 29 and m == 2:
		if bissexto:
			ds= 29
			ms= m 
		else:
			ds= 1
			ms= m + 1
	elif ds == 30 and m == 2:
		ds= 1
		ms= m + 1
	return ds, ms, ad


def diasdomes(m, a):
	dias= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	ndias= dias [m]
	if m == 2 and bissexto(a):
		ndias= 29
	return ndias

a= int( input('Ano: '))
m= int( input('Mês: '))
d= int( input('Dia: '))

da= diaanterior(d, m, a)
ds= diaseguinte(d, m, a)

print('Dia Anterior= ', da, 'Dia Seguinte= ', ds)
