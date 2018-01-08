def polinomio(x,a,b,c):
	y= a*x**2+b*x+c
	return y

def main():
	a=float(input('a= '))
	b=float(input('b= '))
	c=float(input('c= '))
	x=float(input('x= '))

	z=polinomio(x,a,b,c )

	print('resultado de f({})={}'.format(x,z))

main()

