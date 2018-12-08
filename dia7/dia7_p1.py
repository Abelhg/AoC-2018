# Advent Of Code: Dia 7 - Primera parte

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

# Halla el orden necesario para satisfacer todos los pasos
solucion = ""
hechos = set()
while len(pasos.keys()) > 0:
	claves = pasos.keys()
	claves.sort()
	for paso in claves:
		if set(pasos[paso]) <= hechos:
			sigPaso = paso
			break
	pasos.pop(sigPaso)
	hechos.add(sigPaso)
	solucion += sigPaso

print "Solucion:", solucion