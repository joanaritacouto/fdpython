from random import randint
x = randint (1, 100)
print(x)
contagem=1

y = int (input ('Tentativa: '))

while y!=x:
  
  if y>x:
   print('Mais baixo menino(a)! Tenta outra vez!')
  elif y<x:
   print('Mais alto menino(a)! Tenta outra vez!')

  y = int (input ('Tentativa: '))
  contagem=contagem+1

print('acertou miserável!')

print('contagem: ', contagem)
