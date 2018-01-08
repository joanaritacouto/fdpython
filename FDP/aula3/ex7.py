def bissexto(a):
	if (a%4==0 and a%100!=0) or a%400==0:
		return True
	else:
		return False
def diasdomes (m,a):
	dias = [0,31, 28, 31,30, 31, 30, 31, 31, 30, 31, 30, 31]
	ndias = dias [m]

	if m==2 and bissexto(a):
		ndias = 29
	return ndias
		
a = int(input('ano: '))
m = int(input('mês: '))

diasdomes(m,a)

print('o mês {} do ano {} tem {} dias'.format(m, a, diasdomes(m,a)))