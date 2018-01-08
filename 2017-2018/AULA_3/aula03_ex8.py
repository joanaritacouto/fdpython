#endocing:utf8

dia=int(input("Insira o dia: "))
mes=int(input("Insira o mês: "))
ano=int(input("Insira o ano: "))
print("A data que escolheu foi {}-{}-{}".format(dia,mes,ano))

if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes ==11:
	if dia !=1 and dia !=31:
		print("{}-{}-{}".format(dia-1,mes,ano))
		print("{}-{}-{}".format(dia+1,mes,ano))
		
	elif dia==1:
		if mes==1:
			print("{}-{}-{}".format(31,12,ano-1))
			print("{}-{}-{}".format(dia+1,mes,ano))
		elif mes==3:
			if (ano%4==0 and ano%100!=0) or (ano%400==0):
				print("{}-{}-{}".format(29,mes-1,ano))
				print("{}-{}-{}".format(dia+1,mes,ano))
			else:
				print("{}-{}-{}".format(28,mes-1,ano))
				print("{}-{}-{}".format(dia+1,mes,ano))
		elif mes==8:
			print("{}-{}-{}".format(31,mes-1,ano))
			print("{}-{}-{}".format(dia+1,mes,ano))
		else:
			print("{}-{}-{}".format(30,mes-1,ano))
			print("{}-{}-{}".format(dia+1,mes,ano))
	elif dia==31:
		if mes==12:
			print("{}-{}-{}".format(dia-1,mes,ano))
			print("{}-{}-{}".format(1,1,ano+1))
		else:
			print("{}-{}-{}".format(dia-1,mes,ano))
			print("{}-{}-{}".format(1,mes+1,ano))
	
elif mes==4 or mes==6 or mes==9 or mes==11:
	if dia !=1 and dia !=30:
		print("{}-{}-{}".format(dia-1,mes,ano))
		print("{}-{}-{}".format(dia+1,mes,ano))
	
	elif dia==1:
		print("{}-{}-{}".format(31,mes-1,ano))
		print("{}-{}-{}".format(dia+1,mes,ano))
	elif dia==30:
		print("{}-{}-{}".format(dia-1,mes,ano))
		print("{}-{}-{}".format(1,mes+1,ano))
	
	
elif mes==2 and ((ano%4==0 and ano%100!=0) or (ano%400==0)):
	if dia !=1 and dia !=29:
		print("{}-{}-{}".format(dia-1,mes,ano))
		print("{}-{}-{}".format(dia+1,mes,ano))
	elif dia==1:
		print("{}-{}-{}".format(31,mes-1,ano))
		print("{}-{}-{}".format(dia+1,mes,ano))
	elif dia==29:
		print("{}-{}-{}".format(dia-1,mes,ano))
		print("{}-{}-{}".format(1,mes+1,ano))
	
else:
	if dia !=1 and dia !=28:
		print("{}-{}-{}".format(dia-1,mes,ano))
		print("{}-{}-{}".format(dia+1,mes,ano))
	elif dia==1:
		print("{}-{}-{}".format(31,mes-1,ano))
		print("{}-{}-{}".format(dia+1,mes,ano))
	elif dia==28:
		print("{}-{}-{}".format(dia-1,mes,ano))
		print("{}-{}-{}".format(1,mes+1,ano))
