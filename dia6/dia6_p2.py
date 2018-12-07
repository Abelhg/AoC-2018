# Advent Of Code: Dia 6 - Segunda parte

def distManhattan((x1, y1), (x2, y2)):
	return abs(x2-x1) + abs(y2-y1)

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

# Recuento de las posiciones que cumplen que la suma de las distancias Manhattan no supera 10000.
solucion = 0
max_sum = 10000

for i in range(len(MAPA)):
	for j in range(len(MAPA[0])):
		# Obtiene la suma de distancias Manhattan
		suma = 0
		for coord in inp:
			coords = coord.split(', ')
			suma += distManhattan((j+MINX, i+MINY), (int(coords[0]), int(coords[1])))

		if suma < max_sum:
			solucion += 1

print "Solucion:", solucion