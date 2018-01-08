#encoding:utf8

#primeiro piso 3*4metros
#segundo piso 6*4metros
#terceiro piso 9*4metros

distancia_diaria_metros=3*4+6*4+9*4
distancia_diaria_km=distancia_diaria_metros/1000
distancia_anual_km=distancia_diaria_km*365

tempo_percorrido_anualmente_segundos=(distancia_diaria_metros*365)
tempo_percorrido_anualmente_horas=tempo_percorrido_anualmente_segundos/3600


print("O elevador percorre {:.2f} Km por ano.".format(distancia_anual_km))
print("O elevador esteve em funcionamento {:.2f} horas num ano.".format(tempo_percorrido_anualmente_horas))
