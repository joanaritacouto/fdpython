def tax(r):

	if r<=1000:
		y=0.1*r
	elif 1000<r<=2000:
		y=0.2*r-100
	elif r>2000:
		y=0.3*r-300

	return y	
r = float(input('r= '))

y=tax(r)
print('tax(r)= ',y)