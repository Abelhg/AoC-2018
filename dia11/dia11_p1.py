# Advent Of Code: Dia 11 - Primera parte

# Nivel de potencia en una celda:
#  	ID = X + 10
#	Pot = ((ID * Y) + SERIAL) * ID
# 	Pot = ((Pot / 100) % 10) - 5
def potencia(X, Y, SERIAL):
	ID = X + 10
	POT = ((ID * Y) + SERIAL) * ID
	return ((POT / 100) % 10) - 5

# Suma de los valores de un cuadrado de una matriz
def sumaCuadrado(X, Y, MATRIZ, DIMENSION):
	res = 0
	for i in range(DIMENSION):
		for j in range(DIMENSION):
			res += MATRIZ[Y+i][X+j]

	return res

ENTRADA = 1718
# Genera valores de la rejilla
rejilla = []
DIM = 300
for i in range(DIM):
	fila = []
	for j in range(DIM):
		fila.append(potencia(j, i, ENTRADA))

	rejilla.append(fila)

MAXV = -45
SOL = (0, 0)
# Busca el cuadrado 3x3 con mayor suma de potencias
for i in range(DIM-2):
	for j in range(DIM-2):
		# Itera sobre esquinas izquierdas superiores
		suma = sumaCuadrado(j, i, rejilla, 3)

		if suma > MAXV:
			MAXV = suma
			SOL = (j, i)

print "Solucion: " + str(SOL)