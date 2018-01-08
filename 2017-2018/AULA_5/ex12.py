def fibonacci():
	f0=0
	f1=1

	if n==0:
		fn=0

	elif n==1:
		fn==1

	elif n>=2:
		for i in range(n-1):
			fn=f0+f1
			f0=f1
			f1=fn
	return fn
			
n= int(input('número: '))
print(fibonacci())  


