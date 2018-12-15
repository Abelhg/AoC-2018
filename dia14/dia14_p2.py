# Advent Of Code: Dia 14 - Segunda parte

ENTRADA = "190221"
iEnt = 0
RECETAS = [3, 7]
elfo1 = 0
elfo2 = 1
l = 2
solucion = 0
salir = False
while not salir:
	n = str(RECETAS[elfo1] + RECETAS[elfo2])
	for c in n:
		#print "Metiendo '" + c + "'" + "  " + str(iEnt) + "  " + str(solucion)
		if c == ENTRADA[iEnt]:
			iEnt += 1
			#print "Sep:", iEnt, c
			if iEnt >= len(ENTRADA):
				salir = True
				solucion =  len(RECETAS) - len(ENTRADA) + 1
				break
		elif c == ENTRADA[0]:
			iEnt = 1
			#print "Sep, a empezar:", iEnt, c
		else:
			#print "Nope:", iEnt, c
			iEnt = 0
		RECETAS.append(int(c))

		l += 1
	elfo1 = (elfo1 + RECETAS[elfo1] + 1) % l
	elfo2 = (elfo2 + RECETAS[elfo2] + 1) % l

print "Solucion:", solucion