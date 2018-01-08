#encoding:utf8

tempo_inicial_min=52+6*60
tempo_percurso_min=10+6*3+10*4
tempo_final_min=tempo_inicial_min+tempo_percurso_min

tempo_final_horas_min_seg_h=tempo_final_min//60
tempo_final_horas_min_seg_m=tempo_final_min%60
tempo_final_horas_min_seg_s=tempo_final_horas_min_seg_m*60

print("Se sair de casa às 6:52 chego a casa para o pequeno almoço às {} horas {} minutos {} segundos.".format(tempo_final_horas_min_seg_h,tempo_final_horas_min_seg_m,tempo_final_horas_min_seg_s))
