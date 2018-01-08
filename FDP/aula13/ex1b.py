def validar(str):
	return ((len(str)>=3 and str.isdigit()) or (len(str)>=4 and str[0]== '+' and str[1:].isdigit()))


num=input('Número de telefone?')

print(validar(num))		