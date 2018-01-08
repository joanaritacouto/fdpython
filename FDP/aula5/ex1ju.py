def imc(p,a):
	corp=p/a**2
	return corp

def main():
	p= float(input('peso (Kg): '))
	a= float(input('altura (m)'))
	z=imc(p,a)
	
	print('IMC: ', z)

main()