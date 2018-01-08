#ch = caracter
texto = input('qual é o texto? ')

c=texto.split()

d={}

for palavra in c:

 	if palavra in d:
 		d[palavra] += 1
 	else:
 		d[palavra]= 1


print (d)



