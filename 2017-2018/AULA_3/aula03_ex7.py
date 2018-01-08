#encoding:utf8

mes=int(input("Insira o mês: "))
ano=int(input("Insira o ano "))

if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes ==11:
	print("O mês de {} de {} tem 31 dias".format(mes,ano))
	
elif mes==4 or mes==6 or mes==9 or mes==11:
	print("O mês de {} de {} tem 30 dias".format(mes,ano))
	
elif mes==2 and ((ano%4==0 and ano%100!=0) or (ano%400==0)):
	print("O mês de {} de {} tem 29 dias".format(mes,ano))

else:
	print("O mês de {} de {} tem 28 dias".format(mes,ano))
	
	
	
