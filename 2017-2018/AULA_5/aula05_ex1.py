#encoding:utf8

def IMC(p,a):
	IMC=p/(a**2)
	return IMC
	
p=float(input("Peso(Kg): "))
a=float(input("Altura(m): "))
IMC=IMC(p,a)

print("O índice de massa corporal de uma pessoa com {} Kg e {} m de altura é {:.2f}.".format(p,a,IMC))

