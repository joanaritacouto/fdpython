x = int (input ('número: '))
primo = True

for i in range(2,x):
	if x%i ==0:
		primo = False

if primo == True:
	print ('Número primo')

else:
	print ('Número não primo')



  