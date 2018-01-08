#encoding:utf8
import random

x=random.randint(1,100)
print(x)

y=random.random()
y_new=y*101
print(int(y_new))

t=int(input("Digite a sua tentativa: "))
cont=1
 
while t!=x:
	if t>x:
		print("A sua tentativa é demasiado alta!")
	if t<x: 
		print("A sua tentativa é demasiado baixa!")
	t=int(input("Digite a sua próxima tentativa é: "))
	cont=cont+1
	
print("Ao fim de {} tentativas acertou no numero {}.".format(cont,x))
