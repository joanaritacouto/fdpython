#encoding:utf8

#contagem decrescente

n=int(input("Insira o numero pelo qual quer começar a contagem: "))
"""
while n>=0:
	print(n)
	n=n-1
"""	

while True:
	print(n)
	if n<0:
		break
	n=n-1
