soma= 0.0
media=0.0
n=0 


while True:
	
	l =float(input('largura: '))
	c =float(input('comprimento: '))
	

	if (l==0) or (c==0):
		break

	def area(l,c):
	 area= l*c
	 return area
	#print('área de um retângulo: ', area(l, c))
	a= area(l, c)
	soma=soma+a
	n= n+1
	maior=a


	if a>=maior:
		maior=a
	else:
		maior=maior	
		

media=soma/n

print('soma das áreas: ', soma)
print('maior das áreas: ', maior)
print('média das áreas: ',media)