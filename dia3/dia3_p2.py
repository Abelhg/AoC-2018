# Advent Of Code: Dia 3 - Segunda parte

# Genera el tablero
TAM = 1200
tablero = []
for i in range(TAM):
	tablero.append(TAM*['.'])

# Lee entrada
with open('entradaDia3') as f:
	inp = f.readlines()

POSIBLES_IDS = []

# Formato datos: #ID @ (MARGLEFT, MARGTOP): ANCHOxALTO
for l in inp:
	campos = l.split()
	# ID ignorado
	ID = int(campos[0].split('#')[1])
	# Margenes
	margs = campos[2].split(':')[0].split(',')
	margLeft = int(margs[0])
	margTop = int(margs[1])
	# Dimensiones
	dims = campos[3].split('x')
	ancho = int(dims[0])
	alto = int(dims[1])
	# Lo mete en el tablero a partir de los margenes
	borrado = False
	for i in range(margTop, margTop + alto):
		for j in range(margLeft, margLeft + ancho):
			if tablero[i][j] == '.':
				# Vacio
				tablero[i][j] = ID
				if ID not in POSIBLES_IDS and not borrado:
					POSIBLES_IDS.append(ID)
			elif tablero[i][j] != 'X':
				# Con una
				if ID in POSIBLES_IDS:
					POSIBLES_IDS.remove(ID) # Borra el actual
				if tablero[i][j] in POSIBLES_IDS:
					POSIBLES_IDS.remove(tablero[i][j])
				borrado = True
				tablero[i][j] = 'X'

print "Solucion:", POSIBLES_IDS[0]