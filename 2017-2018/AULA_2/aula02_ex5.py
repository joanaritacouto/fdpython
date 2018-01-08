# encoding:utf8

d=float(input("Insira a distancia que percorreu em milhas: "))
tempo_minutos=float(input("Insira quantos minutos demorou no percurso: "))

d_km=d*1.61
tempo_horas=tempo_minutos/60

tempo_medio_km=tempo_horas/d_km

vm=d_km/tempo_horas

print("O tempo medio por Km é {:.3} h/Km.".format(tempo_medio_km))

print("A velocidade média é {:.3} Km/h.".format(vm))
