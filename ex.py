#calcular a area até o utilizador c=0 e no final devolver a media de todas calculadas e a maior area


def area (c,l):
  a=c*l
  return a 

c=1
cont=0
soma=0
maior=0
while c!=0: 
  l = int (input ('lado:'))
  c = int (input ('comprimento:'))
  if c==0:
    break 
  cont=cont+1
  a= area(c,l)
  soma=soma+a
  if a>maior:
    maior=a
  print ('Area= ', a, 'maior area= ', maior)

media=soma/cont

print ('media= ', media) 






 
