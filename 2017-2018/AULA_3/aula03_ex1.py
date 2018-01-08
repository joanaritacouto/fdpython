#encoding:utf8 

AP1=float(input("Qual a nota da avaliação AP1? "))
ATP=float(input("Qual a nota da avaliação ATP? "))
EP=float(input("Qual a nota da avaliação EP? "))

nota_final=(AP1*0.3+ATP*0.3+EP*0.4)
print("A sua nota final é {:.2f}.".format(nota_final))

if nota_final >= 9.5:
	print("O aluno está aprovado!")
	
else:
	print("O aluno está reprovado!")
	
