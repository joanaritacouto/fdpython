#encoding:utf8

import math

cateto_A=float(input("Insira o valor do cateto A: "))
cateto_B=float(input("Insira o valor do cateto B: "))

hipotenusa=math.sqrt(cateto_A**2+cateto_B**2)

cosseno_theta=cateto_A/hipotenusa

theta=math.acos(cosseno_theta)
theta_graus=(theta*360)/(2*math.pi)

print("O valor da hipotenusa cujos catetos são {} e {} é {}.".format(cateto_A,cateto_B,hipotenusa))

print("O angulo compreendido entre o lado A e a hipotenusa mede {:.2f} graus".format(theta_graus))
