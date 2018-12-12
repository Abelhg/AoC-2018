# Advent Of Code: Dia 11 - Segunda parte

# Este lleva un ratito en llegar a la solucion.

# Nivel de potencia en una celda:
#  	ID = X + 10
#	Pot = ((ID * Y) + SERIAL) * ID
# 	Pot = ((Pot / 100) % 10) - 5
def potencia(X, Y, SERIAL):
	ID = X + 10
	POT = ((ID * Y) + SERIAL) * ID
	return ((POT / 100) % 10) - 5

ENTRADA = 1718
# Genera valores de la rejilla
rejilla = []
DIM = 300
for i in range(DIM):
	fila = []
	for j in range(DIM):
		fila.append(potencia(j, i, ENTRADA))

	rejilla.append(fila)

# Datos calculados. Programacion dinamica
BASE = []
for i in range(DIM):
	BASE.append(list(rejilla[i]))

maxvals = []
sols = []
# Itera sobre tamanos de cuadrados
for d in range(2,DIM):
	maxvalint = -999999
	intsol = (0,0)
	# Busca el cuadrado 3x3 con mayor suma de potencias
	for i in range(DIM-d+1):
		for j in range(DIM-d+1):
			# Itera sobre esquinas izquierdas superiores
			suma = BASE[i][j] # Usa dato anterior
			# Y calcula solo la ultima fila y columna
			for k in range(d):
				suma += rejilla[i+d-1][j+k]
			for k in range(d-1):
				suma += rejilla[i+k][j+d-1]
			# Actualiza valor
			BASE[i][j] = suma 
			if suma > maxvalint:
				maxvalint = suma
				intsol = (j, i)
	maxvals.append(maxvalint)
	sols.append(intsol)

MAXV = max(maxvals)
SOL = sols[maxvals.index(MAXV)]
print "Solucion: " + str(SOL) + ", " + str(maxvals.index(MAXV)+2)