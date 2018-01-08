
def main():  #1.a
	d = {}
	menu = """
	1) Registar chamada
	2) Ler ficheiro
	3) Listar clientes
	4) Fatura
	5) Terminar
	0) Opção?
	"""
	op = int(input(menu))
		while True:
			if op == 1:
				d = {}
				registar(d)

			elif op == 5:
				print ('FIM')
				break

			else:
				print(opção inválida) 

def validar(num):  #1.b
	if (len(num)>=3):

		if (num[0]== "+"):
			return (num[1:].isdigit() and len(num)>=4)

		else:
			return (num[0:].isdigit())

	else:
		return False		
				
def registar(d):  #1.c
	validade = False
	while not validade :
		numOrigem = input ('número de origem? ')
		validade = validar(numOrigem)

	# at this point, numOrigem is surely valid!
	validade = False
	while not validade:
		numDestino = input ('número de destino? ')
		validade = validar(numDestino)

	# at this point, both numbers are valid!
	duração = input ('duração? ')
	if numOrigem not in d.keys():
		d[numOrigem] = []
	d[numOrigem].append({"destino": numDestino, "duracao" : duração})
	return d

def lerFicheiros(ficheiro):
	file = open(ficheiro,'r')
	for line in file:
		parts = line.strip().split()

	
 




	

		



