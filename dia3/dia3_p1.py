# Advent Of Code: Dia 3 - Primera parte

# Genera el tablero
TAM = 1000
tablero = []
for i in range(TAM):
	tablero.append(TAM*['.'])

# Lee entrada
with open('entradaDia3') as f:
	inp = f.readlines()

# Formato datos: #ID @ (MARGLEFT, MARGTOP): ANCHOxALTO
for l in inp:
	campos = l.split()
	# ID ignorado
	# Margenes
	margs = campos[2].split(':')[0].split(',')
	margLeft = int(margs[0])
	margTop = int(margs[1])
	# Dimensiones
	dims = campos[3].split('x')
	ancho = int(dims[0])
	alto = int(dims[1])
	# Lo mete en el tablero a partir de los margenes
	for i in range(margTop, margTop + alto):
		for j in range(margLeft, margLeft + ancho):
			if tablero[i][j] == '.':
				# Vacio
				tablero[i][j] = '#'
			elif tablero[i][j] == '#':
				# Con una
				tablero[i][j] = 'X'

# Hace un recuento de las solapadas
recuento = 0
for fila in tablero:
	for colu in fila:
		if colu == 'X':
			recuento += 1
print "Solucion:", recuento