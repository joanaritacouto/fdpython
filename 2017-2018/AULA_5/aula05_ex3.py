#encoding:utf8

def polinomio(x,a,b,c):
	polinomio= a*(x)**2 + b*x + c
	return polinomio
	
p1=polinomio(0,1,2,3)
print("O valor do polinomio quando x é 0 é: ",p1)


	
p2=polinomio(0.1,1,2,3)
print("O valor do polinomio quando x é 0.1 é: ",p2)


	
p3=polinomio(2,1,2,3)
print("O valor do polinomio quando x é 2 é: ",p3)
