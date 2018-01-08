# encoding:utf8

tempo=int(input("Digite o numero de segundos que deseja converter: "))

horas=tempo//3600

minutos=(tempo%3600)//60

segundos=(tempo%3600)%60

print("{:.0f}h:{:.0f}min:{:.0f}seg".format(horas,minutos,segundos))
