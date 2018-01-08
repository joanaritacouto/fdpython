def menu():
		x=int(input('1-Registar chamada\n2-Ler ficheiro\n3-Listar clientes\n4-Fatura\n5-Terminar\nOpção?'))

		return x

def main():
	terminar=False

	while not terminar:
		op=menu()

		if op==1:
			print('1')

		elif op==2:
			print('2')

		elif op==3:
			print('3')

		elif op==4:
			print('4')

		elif op==5:
			terminar = True

main()

def validar(str):
	return ((len(str)>=3 and str.isdigit()) or (len(str)>=4 and str[0]== '+' and str[1:].isdigit()))
def numero():
	while True: 
	num=input('Número de telefone?')

print(validar(num))		

