# Advent Of Code: Dia 14 - Primera parte

ENTRADA = 190221
RECETAS = [3, 7]
elfo1 = 0
elfo2 = 1
l = 2

salir = False
while not salir:
	n = str(RECETAS[elfo1] + RECETAS[elfo2])
	for c in n:
		RECETAS.append(int(c))
		l += 1
	elfo1 = (elfo1 + RECETAS[elfo1] + 1) % l
	elfo2 = (elfo2 + RECETAS[elfo2] + 1) % l

	if l >= ENTRADA+10:
		salir = True
	
solucion = ""
for i in range(ENTRADA, ENTRADA+10):
	solucion += str(RECETAS[i])

print "Solucion:", solucion