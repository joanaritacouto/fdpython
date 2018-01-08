#encoding:utf8

import math

abcissa_p1=float(input("Insira o valor da abcissa do ponto 1: "))

ordenada_p1=float(input("Insira o valor da ordenada do ponto 1: "))

abcissa_p2=float(input("Insira o valor da abcissa do ponto 2: "))

ordenada_p2=float(input("Insira o valor da ordenada do ponto 2: "))

dist_p1_p2=math.sqrt((abcissa_p2-abcissa_p1)**2+(ordenada_p2-ordenada_p1)**2)

print("A distÂncia entre os pontos P1 de coordenadas ({},{}) e P2 de coordenadas ({},{}) é {:.2f}.".format(abcissa_p1,ordenada_p1,abcissa_p2,ordenada_p2,dist_p1_p2))
