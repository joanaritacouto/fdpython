#encoding:utf8

#argumentos são atribuídos a parâmetros
"""
def soma(x,y):  # x e y são dois argumentos que são atribuidos a 2 parâmetros
	soma=x+y
	return soma
	
x=float(input("Digite o valor de x: "))
y=float(input("Digite o valor de y: "))
print(soma(x,y))

#ou 

def soma(x,y):
	soma=x+y
	return soma

print(soma(5,6))
"""

#Keyword argument

def printinfo(name,age):
	print("Nome: ",name)
	print("Idade: ", age)
	
printinfo("Mariana",20)
printinfo(age=20,name="Mariana")

#Default argument

def printinfo(name,age=16):
	print("Nome: ",name)
	print("Idade: ", age)
	
printinfo("Mariana")   #idade vai adquirir o valor 16
printinfo("Mariana",20)

#argumento de tamanho variável

def printinfo(arg1,*vartuple):
	print (arg1)
	for var in vartuple:
		print(var)
		
printinfo(10,20,30)

#funçoes anónimas

sum=lambda arg1,arg2:arg1*arg2

print(sum(4,5))

