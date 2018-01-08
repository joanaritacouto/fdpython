#encoding:utf8

l=float(input("Insira a quantidade de litros de combustível que abasteceu: "))



if l > 40:
	preco=(1.4*40)+(1.4*0.9*(l-40))
	print("O preço a pagar é {:.2f} .".format(preco))
	
else:	
	preco=1.4*l
	print("O preço a pagar é {:.2f} .".format(preco))
	
