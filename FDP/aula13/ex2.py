def main():
	jogo={}
	file = open('Jornadas.csv', 'r')

	for line in file:
		partes = line.strip().split(',')
		if partes[0] in jogo:
			jogo[partes[0]].append((partes[1],partes[2]))
		else:
			jogo[partes[0]]=[ (partes[1],partes[2]) ]	

	file.close()

	num=9
	while num > 0:
		jornada = int(input('Jornada?'))

		if jornada <= 13 and jornada > 0:
			apostas = {}
			jornada=str(jornada)
			jogos = jogo[jornada]
			for i, j in enumerate(jogos):
				a = "-"
				while a != "1" and a != "2" and a != "X":
					texto = " ".join([str(i+1), j[0], "vs", j[1], ": "])
					a = input(texto)

				apostas[str(i+1)] = a
			# todas as apostas foram feitas, agora vamos guardar
			ficheiro = "Jornada"+jornada+".csv"
			fp = open(ficheiro, "w+")
			for k, a in sorted(apostas.items()):
				linha = k + "," + a
				fp.write(linha+"\n")
			fp.close()

			num = num - 1 

		
main()
