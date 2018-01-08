def polinomio(x):
	y=x**2+2*x+3
	return y

a = [0, 0.1, 2]

for i in a:
	res = polinomio(i)
	print('f({})={}'.format(i, res))


