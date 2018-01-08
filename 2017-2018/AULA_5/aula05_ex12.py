#encoding:utf8

def fibonacci():
	f0=0
	f1=1
	if n==0:
		f_new=0
	elif n==1:
		f_new=1
	elif n>=2:
		for i in range(n-1):
			f_new=f0+f1
			f0=f1
			f1=f_new
	return f_new
	
	
n=int(input("Insira o n-ésimo número para o qual quer calcular na sequencia Fibonacci: "))
print(fibonacci())  
