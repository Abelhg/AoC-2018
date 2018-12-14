# Advent Of Code: Dia 13 - Primera parte

# Lee entrada
with open('entradaDia13') as f:
	inp = f.readlines()

DER = ">"
IZQ = "<"
ARR = "^"
ABA = "v"
MAPA = []
CARROS = []
for i in range(len(inp)):
	linea = list(inp[i].split('\n')[0])
	encontrados = True
	while encontrados:
		encontrados = False
		iD = iI = iAr = iAb = -1
		try:
			iD = linea.index(DER)
		except ValueError:
			pass
		try:
			iI = linea.index(IZQ)
		except ValueError:
			pass
		try:
			iAr = linea.index(ARR)
		except ValueError:
			pass
		try:
			iAb = linea.index(ABA)
		except ValueError:
			pass

		if iD != -1:
			CARROS.append([iD, i, DER, 0])
			linea[iD] = '-'
			encontrados = True
		if iI != -1:
			CARROS.append([iI, i, IZQ, 0])
			linea[iI] = '-'
			encontrados = True
		if iAr != -1:
			CARROS.append([iAr, i, ARR, 0])
			linea[iAr] = '|'
			encontrados = True
		if iAb != -1:
			CARROS.append([iAb, i, ABA, 0])
			linea[iAb] = '|'
			encontrados = True

	MAPA.append(linea)

# Bucle principal
colision = False
solucion = (-1,-1)
while not colision:
	# Ordena carros: los superiores primero
	CARROS = sorted(CARROS, key=lambda c:c[1])

	for carro in CARROS:
		pos = carro[2]
		if pos == DER:
			sig = MAPA[carro[1]][carro[0]+1]
			if sig == '/':
				carro[2] = ARR
			elif sig == '\\':
				carro[2] = ABA
			elif sig == '+':
				if carro[3] == 0:
					carro[2] = ARR
				elif carro[3] == 2:
					carro[2] = ABA
				carro[3] = (carro[3] + 1) % 3
			carro[0] += 1
		elif pos == IZQ:
			sig = MAPA[carro[1]][carro[0]-1]
			if sig == '/':
				carro[2] = ABA
			elif sig == '\\':
				carro[2] = ARR
			elif sig == '+':
				if carro[3] == 0:
					carro[2] = ABA
				elif carro[3] == 2:
					carro[2] = ARR
				carro[3] = (carro[3] + 1) % 3

			carro[0] -= 1
		elif pos == ARR:
			sig = MAPA[carro[1]-1][carro[0]]
			if sig == '/':
				carro[2] = DER
			elif sig == '\\':
				carro[2] = IZQ
			elif sig == '+':
				if carro[3] == 0:
					carro[2] = IZQ
				elif carro[3] == 2:
					carro[2] = DER
				carro[3] = (carro[3] + 1) % 3

			carro[1] -= 1
		elif pos == ABA:
			sig = MAPA[carro[1]+1][carro[0]]
			if sig == '/':
				carro[2] = IZQ
			elif sig == '\\':
				carro[2] = DER
			elif sig == '+':
				if carro[3] == 0:
					carro[2] = DER
				elif carro[3] == 2:
					carro[2] = IZQ
				carro[3] = (carro[3] + 1) % 3

			carro[1] += 1

		# Comprueba colision
		for carro2 in CARROS:
			if carro != carro2:
				if carro[0] == carro2[0] and carro[1] == carro2[1]:
					colision = True
					solucion = (carro[0], carro[1])
					break

print "Solucion:", solucion