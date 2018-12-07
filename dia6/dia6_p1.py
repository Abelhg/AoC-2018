# Advent Of Code: Dia 6 - Primera parte

# Halla el punto mas cercano
def buscaCercano(mapa, x, y):
	nivel = 1

	while True:
		pos_res = []
		# Comienza desde la esquina izquierda
		crecX = 1
		crecY = 1
		X = x - nivel
		Y = y
		for cont in range(nivel * 4):
			if X >= 0 and X < len(mapa[0]) and Y >= 0 and Y < len(mapa):
				# Esta dentro del mapa
				if mapa[Y][X] != '.' and '_' not in mapa[Y][X]:
					pos_res.append(mapa[Y][X])

			X += crecX
			Y += crecY

			if abs(X-x) > nivel:
				crecX *= -1
				X += (2 * crecX)
			if abs(Y-y) > nivel:
				crecY *= -1
				Y += (2 * crecY)	

		# Al acabar de sondear el nivel, comprueba si hay resultado
		if len(pos_res) == 1:
			# Coordenada original -> se asigna y termina
			mapa[y][x] = pos_res[0] + "_" + str(nivel)
			return
		elif len(pos_res) > 1:
			# 2 o mas resultados -> se coloca '.'
			mapa[y][x] = '.'
			return

		nivel += 1

# Lee entrada
with open('entradaDia6') as f:
	inp = f.readlines()

MINX = -1
MAXX = -1
MINY = -1
MAXY = -1

# Busca menor valor de X e Y
for i in inp:
	coords = i.split('\n')[0]
	X = int(coords.split(',')[0])
	Y = int(coords.split(',')[1])
	if X < MINX or MINX == -1:
		MINX = X
	if X > MAXX or MAXX == -1:
		MAXX = X
	if Y < MINY or MINY == -1:
		MINY = Y
	if Y > MAXY or MAXY == -1:
		MAXY = Y

# Genera mapa inicial vacio
MAPA = []
vacio = (MAXX - MINX + 1) * ['.']
for i in range(MAXY-MINY+1):
	MAPA.append(list(vacio))

# Introduce las coordenadas
for i in range(len(inp)):
	coords = inp[i].split('\n')[0]
	X = int(coords.split(',')[0]) - MINX
	Y = int(coords.split(',')[1]) - MINY
	MAPA[Y][X] = str(i)

# Calcula los cercanos
for i in range(len(MAPA)):
	for j in range(len(MAPA[0])):
		if MAPA[i][j] == '.':
			buscaCercano(MAPA, j, i)


# Halla los infinitos y los pone en una lista
infinitos = []
for x in MAPA[0]:
	vals = x.split('_')
	if vals[0] not in infinitos:
		infinitos.append(vals[0])

izq = [row[0] for row in MAPA]
for x in izq:
	vals = x.split('_')
	if vals[0] not in infinitos:
		infinitos.append(vals[0])

der = [row[len(MAPA[0])-1] for row in MAPA]
for x in der:
	vals = x.split('_')
	if vals[0] not in infinitos:
		infinitos.append(vals[0])

for x in MAPA[len(MAPA)-1]:
	vals = x.split('_')
	if vals[0] not in infinitos:
		infinitos.append(vals[0])

# De los no infinitos, hace un recuento buscando el que mas area tiene
solucion = 0
for i in range(len(inp)):
	if str(i) not in infinitos:
		cont = 0
		# Busca su area
		for x in MAPA:
			for y in x:
				if str(i) == y.split('_')[0]:
					cont += 1

		if cont > solucion:
			solucion = cont

print "Solucion:", solucion