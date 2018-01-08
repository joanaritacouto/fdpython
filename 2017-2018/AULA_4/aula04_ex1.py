x = float( input('Qual o seu primeiro numero? ') )
cont = 0
soma = 0
maximo=x
minimo=x

while x != 0:
  soma = soma + x
  cont = cont + 1
  x = float( input('numero: ') )
  if x>maximo:
	  maximo=x
  
  if x<minimo and x!=0:    #se colocasse antes do x escusava de colocar x!=0
	  minimo=x
		
if cont != 0:
  media = soma / cont
else:
  media = 0

print("Foram introduzidos {} elementos e a sua média é {}. O valor máximo introduzido foi {} e o valor minimo introduzido foi {}.".format(cont,media,maximo,minimo))
print('FIM')
