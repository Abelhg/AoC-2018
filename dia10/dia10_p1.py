# Advent Of Code: Dia 10 - Primera parte

# Detecta si los puntos forman texto
def formanTexto(puntos):
	res = True

	for punto in puntos:
		conex = 0
		for p in puntos:
			if punto != p:
				difX = abs(int(punto[0]) - int(p[0]))
				difY = abs(int(punto[1]) - int(p[1]))
				if difX <= 1 and difY <= 1:
					conex += 1
		if conex == 0:
			return False
	return res

# Lee entrada
with open('entradaDia10') as f:
	inp = f.readlines()

estrellas = []
for linea in inp:
	# Extrae datos
	iX = linea.index('<')+1
	iCom = inp[0].index(',')
	iY = linea.index('>')
	PX = int(linea[iX:iCom])	# Coordenada X
	PY = int(linea[iCom+1:iY])	# Coordenada Y
	iX = linea.index('<', iX)+1
	iCom = linea.index(',', iX)
	iY = linea.index('>', iCom)
	VX = int(linea[iX:iCom])	# Velocidad X
	VY = int(linea[iCom+1:iY])	# Velocidad Y
	estrellas.append([PX, PY, VX, VY])

salir = False
while not salir:
	for i in range(len(estrellas)):
		estrella = estrellas[i]
		estrella[0] += estrella[2]
		estrella[1] += estrella[3]
	if formanTexto(estrellas):
		salir = True

MINX = -1
MINY = -1
MAXX = -1
MAXY = -1
for estrella in estrellas:
	PX = estrella[0]
	PY = estrella[1]
	if PY < MINY or MINY == -1:
		MINY = PY
	if PY > MAXY or MAXY == -1:
		MAXY = PY
	if PX < MINX or MINX == -1:
		MINX = PX
	if PX > MAXX or MAXX == -1:
		MAXX = PX
# Tam. cielo
DIMX = MAXX - MINX + 1
DIMY = MAXY - MINY + 1
cielo = []
for i in range(DIMY):
	cielo.append(DIMX * ['.'])

for estrella in estrellas:
	PX = estrella[0]
	PY = estrella[1]
	cielo[PY-MINY][PX-MINX] = '#'

with open("salida", "w") as f:
	for linea in cielo:
		s = ""
		for punto in linea:
			s += punto
		s += "\n"
		f.write(s)

print "Solucion en el archivo de salida."