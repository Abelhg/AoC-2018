# Advent Of Code: Dia 10 - Segunda parte

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
tiempo = 0
while not salir:
	for i in range(len(estrellas)):
		estrella = estrellas[i]
		estrella[0] += estrella[2]
		estrella[1] += estrella[3]
	tiempo += 1
	if formanTexto(estrellas):
		salir = True

print "Solucion:", tiempo