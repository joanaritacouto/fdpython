import math

A = float (input('primeiro cateto: '))
B = float (input('segundo cateto: '))

c = A**2 + B**2 

C = math.sqrt (c)

print ('hipotenusa: ', C)
 
angulo = math.acos (A/C)

print('ângulo: {} rad'.format(angulo))

graus = math.degrees (angulo)

print('ângulo: {} º'.format(graus))

