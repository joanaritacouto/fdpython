#encoding:utf8

n=int(input("Insira o numero que quer testar: "))
cont=0
for i in range(1,n+1):   #gera numeros entre 0 e 9
	if n%i==0:
		cont=cont+1

if cont == 2:
  print('Primo')
else:
  print('NAO')
