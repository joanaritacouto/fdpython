#ch = caracter
mensagem = input('qual é a mensagem? ')
d = {}
for i in range (len(mensagem)):
 	ch= mensagem[i]
 	if ch.isalpha():

 		if ch in d:
 			d[ch] +=1
 		else:
 			d[ch] = 1

print ('contagem dos caracteres da mensagem:')

for ch in d:
	print (ch, d[ch])			