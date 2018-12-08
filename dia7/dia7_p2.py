# Advent Of Code: Dia 7 - Segunda parte

# Lee entrada
with open('entradaDia7') as f:
	inp = f.readlines()

# Genera un diccionario de pasos con sus necesarios anteriores
pasos = {}
for linea in inp:
	partes = linea.split(' ')
	anterior = partes[1] 
	siguiente = partes[7]
	if anterior not in pasos.keys():
		pasos[anterior] = []
	if siguiente not in pasos.keys():
		pasos[siguiente] = [anterior]
	else:
		pasos[siguiente].append(anterior)


minTiempo = 60
numTrabajadores = 5

tiempo = 0
hechos = set()
disponibles = []
actuales = numTrabajadores * ['.']
contActuales = numTrabajadores * [-1]
while len(pasos.keys()) > 0:
	# Actua sobre los trabajadores
	for i in range(len(actuales)):
		if actuales[i] != '.':
			# Trabajador ocupado -> avanza en trabajo
			contActuales[i] -= 1
			if contActuales[i] == 0:
				# Ha acabado trabajo -> se libera
				pasos.pop(actuales[i])
				hechos.add(actuales[i])
				actuales[i] = '.'

		# Busca disponibles
		claves = pasos.keys()
		claves.sort()
		for paso in claves:
			if paso not in actuales and paso not in disponibles and set(pasos[paso]) <= hechos:
				disponibles.append(paso)

		# Comprueba trabajadores libres
		if actuales[i] == '.':
			if len(disponibles) > 0:
				# Trabajador libre -> se usa
				#print "\tSe asigna", disponibles[0], "a trabajador", i
				actuales[i] = disponibles[0]
				contActuales[i] = minTiempo + ord(disponibles[0]) - ord('A') + 1
				disponibles.pop(0)

		i += 1

	tiempo += 1

print "Solucion:", tiempo-2