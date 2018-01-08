#encoding:utf8

c_matematicaA=int(input("Insira a sua classificação de Matemática A: "))
c_fq=int(input("Insira a sua classificação de Fisico Quimica: "))
c_bg=int(input("Insira a sua classificação de Biologia e Geologia: "))
c_filosofia=int(input("Insira a sua classificação de Filosofia: "))
c_portugues=int(input("Insira a sua classificação de Portugues: "))
c_biologia=int(input("Insira a sua classificação de Biologia: "))
c_quimica=int(input("Insira a sua classificação de Quimica: "))
c_ingles=int(input("Insira a sua classificação de Ingles: "))

c_exame_matematica=float(input("Insira a sua classificação no exame de Matemática A: "))
c_exame_fq=float(input("Insira a sua classificação no exame de Fisico Quimica: "))

media_interna=(c_matematicaA+c_fq+c_bg+c_filosofia+c_portugues+c_biologia+c_quimica+c_ingles)/8
media_exames=(c_exame_matematica+c_exame_fq)/2

media_entrada=media_interna*0.5+media_exames*0.5

print("A sua média de entrada é: ", media_entrada)
print("A sua media de entrada é: " + str(media_entrada))
print("A sua média de entrada é: {:.2f}.".format(media_entrada))
