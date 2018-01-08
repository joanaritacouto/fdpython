#encoding:utf8

def countdown(N):
	while N>-1:
		print(N)
		N=N-1
		
N=int(input("Insira um número pelo qual quer começar a contagem: "))
countdown(N)
