# Advent Of Code: Dia 17 - Primera parte

import os
vistaX = 400
vistaY = 0
dimX = 169
dimY = 40

def imprimeMapa(mapa, x, y, dimx, dimy):
	for i in range(dimy):
		s = ""
		for j in range(dimx):
			s += mapa[y+i][x+j]
		print s

ARCILLA = "#"
ARENA = "."
CAIDA = "|"
ESTANCADA = "~"
sFUENTE = "+"
FUENTE = (500, 0)
class Gota:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.estado = CAIDA

# Lee entrada
with open('entradaDia17') as f:
	inp = f.readlines()

# Crea los bloques de arcilla
ARCILLAS = []
for linea in inp:
	x = -1
	y = -1
	vals = linea.rstrip().split(", ")
	v = vals[0].split('=')
	if v[0] == 'x':
		x = int(v[1])
	else:
		y = int(v[1])
	seg = vals[1][2:].split("..")
	if x != -1:
		for i in range(int(seg[0]), int(seg[1])+1):
			ARCILLAS.append((x, i))
	else:
		for i in range(int(seg[0]), int(seg[1])+1):
			ARCILLAS.append((i, y))

MINX = min(ARCILLAS, key=lambda a: a[0])[0] - 1
MINY = min(ARCILLAS, key=lambda a: a[1])[1]
MAXX = max(ARCILLAS, key=lambda a: a[0])[0] + 1
MAXY = max(ARCILLAS, key=lambda a: a[1])[1]
MAPA = []
for i in range(MAXY+1):
	MAPA.append([ARENA] * (MAXX-MINX+1))

for a in ARCILLAS:
	MAPA[a[1]][a[0] - MINX] = ARCILLA

g = Gota(FUENTE[0], FUENTE[1] + 1)
GOTAS_GEN = [ g ]

MAPA[FUENTE[1]][FUENTE[0] - MINX] = sFUENTE
MAPA[g.y][g.x - MINX] = g.estado

# En cada iteracion se suma una gota por cada gota generadora
while len(GOTAS_GEN) != 0:
	nGen = []
	for gota_gen in GOTAS_GEN:
		nuevas = []
		if gota_gen.y + 1 <= MAXY:
			# Comprueba limite
			debajo = MAPA[gota_gen.y+1][gota_gen.x - MINX]
			if debajo != ARCILLA and debajo != CAIDA and debajo != ESTANCADA:
				# Genera gota debajo
				g = Gota(gota_gen.x, gota_gen.y + 1)
				nuevas.append(g)
				MAPA[gota_gen.y+1][gota_gen.x - MINX] = g.estado
			else:
				# A los lados
				derecha = MAPA[gota_gen.y][gota_gen.x - MINX + 1]
				if derecha != ARCILLA and derecha != CAIDA and derecha != ESTANCADA:
					# Genera gota derecha
					g = Gota(gota_gen.x + 1, gota_gen.y)
					nuevas.append(g)
					MAPA[gota_gen.y][gota_gen.x - MINX + 1] = g.estado
				
				izquierda = MAPA[gota_gen.y][gota_gen.x - MINX - 1]
				if izquierda != ARCILLA and izquierda != CAIDA and izquierda != ESTANCADA:
					# Genera gota izquierda
					g = Gota(gota_gen.x - 1, gota_gen.y)
					nuevas.append(g)
					MAPA[gota_gen.y][gota_gen.x - MINX - 1] = g.estado
			
			if len(nuevas) != 0:
				nGen += nuevas
			else:
				# Puede que haya estancamiento
				y = gota_gen.y
				estancadoIzq = False
				estancadoDer = False
				xIzq = gota_gen.x - 1
				xDer = gota_gen.x + 1
				salir = False
				while not salir:
					# Busca a los lados dos paredes o arena
					if not estancadoIzq:
						if MAPA[y][xIzq - MINX] == ARCILLA:
							estancadoIzq = True
							if estancadoDer:
								salir = True
						elif (MAPA[y][xIzq - MINX] != CAIDA and 
							  MAPA[y][xIzq - MINX] != ESTANCADA):
							# Arena
							salir = True
						else:
							xIzq -= 1
					
					if not estancadoDer:
						if MAPA[y][xDer - MINX] == ARCILLA:
							estancadoDer = True
							if estancadoIzq:
								salir = True
						elif (MAPA[y][xDer - MINX] != CAIDA and 
							  MAPA[y][xDer - MINX] != ESTANCADA):
							# Arena
							salir = True
						else:
							xDer += 1

				if estancadoIzq and estancadoDer:
					# Hay estancamiento
					xIzq += 1
					nivel = gota_gen.y
					while xIzq < xDer:
						MAPA[nivel][xIzq - MINX] = ESTANCADA
						if MAPA[nivel-1][xIzq - MINX] == CAIDA:
							nuevas.append(Gota(xIzq, nivel-1))

						xIzq += 1
					nGen += nuevas

	GOTAS_GEN = nGen

	
	# Control de vista
        while True:
		os.system("clear")
		imprimeMapa(MAPA, vistaX - MINX, vistaY, dimX, dimY)
		cmd = raw_input()
		if len(cmd) == 0:
			break
		else:
			for c in cmd:
				if c == "d":
					if vistaX + dimX - MINX < len(MAPA[0]):
						vistaX += 1
				elif c == "a":
					if vistaX - MINX > 0:
						vistaX -= 1     
				elif c == "w":
					if vistaY > 0:
						vistaY -= 1     
				elif c == "s":
					if vistaY + dimY < len(MAPA):
						vistaY += 1
	

solucion = 0
for i in range(MINY, MAXY+1):
	solucion += MAPA[i].count(CAIDA)
	solucion += MAPA[i].count(ESTANCADA)

print "Solucion:", solucion
