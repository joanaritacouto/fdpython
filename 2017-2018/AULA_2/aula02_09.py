#encoding: utf8

tempo = int(input("Qual o valor do tempo, em segundos, para converter? "))
horas = tempo // 3600
minutos = (tempo - (horas * 3600)) // 60
segundos = tempo - (horas * 3600) - (minutos *60)
print("{}h:{}min:{}s".format(horas, minutos, segundos))
