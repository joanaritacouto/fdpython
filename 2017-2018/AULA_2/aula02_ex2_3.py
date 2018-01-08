# encoding:utf8



#alinea 3

c_matematicaA=17
c_fq=18
c_bg=16
c_filosofia=18
c_portugues=16
c_biologia=18
c_quimica=19
c_ingles=17

c_exame_matematica=16.9
c_exame_fq=17.8

media_interna=(c_matematicaA+c_fq+c_bg+c_filosofia+c_portugues+c_biologia+c_quimica+c_ingles)/8
media_exames=(c_exame_matematica+c_exame_fq)/2

media_entrada=media_interna*0.5+media_exames*0.5

print("A sua média de entrada é: ", media_entrada)
print("A sua media de entrada é: " + str(media_entrada))
print("A sua média de entrada é: {:.2f}.".format(media_entrada))
