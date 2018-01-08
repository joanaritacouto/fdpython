import math 

def potencia(valor, expoente):
	return valor**expoente

def distancia(x1, y1, x2, y2):
	res = math.sqrt(potencia(x1-x2, 2) + potencia(y1-y2, 2))
	return res	

x1 = float (input ('x de p1: '))
y1 = float (input ('y de p1: '))
x2 = float (input ('x de p2: '))
y2 = float (input ('y de p2: '))

a = (x1-x2)**2 + (y1-y2)**2
dist = math.sqrt (a)

# dist = distancia(x1, y1, x2, y2)

print ('distãncia entre os pontos: ', dist)

