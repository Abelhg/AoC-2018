# Advent Of Code: Dia 18 - Primera parte

ARBOLES = "|"
ALMACEN = "#"
CLARO = "."

vecinos = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

# Devuelve el numero de arboles, almacenes y claros para una casilla.
def getDatos(mapa, x, y):
	arb = 0
	alm = 0
	cla = 0
	for v in vecinos:
		if (x + v[0] >= 0 and y + v[1] >= 0 and 
			x + v[0] < len(mapa[0]) and y + v[1] < len(mapa)):
			c = mapa[y + v[1]][x + v[0]]
			if c == ARBOLES:
				arb += 1
			elif c == ALMACEN:
				alm += 1
			elif c == CLARO:
				cla += 1

	return (arb, alm, cla)

# Lee entrada
with open('entradaDia18') as f:
	estado = [l.rstrip() for l in f.readlines()]


MINS = 600
for i in xrange(MINS):
	nuevo = []
	for j in range(len(estado)):
		s = ""
		for k in range(len(estado[0])):
			(arb, alm, cla) = getDatos(estado, k, j)
			if estado[j][k] == ARBOLES and alm >= 3:
				s += ALMACEN
			elif estado[j][k] == ALMACEN:
				if alm > 0 and arb > 0:
					s += ALMACEN
				else:
					s += CLARO
			elif estado[j][k] == CLARO and arb >= 3:
				s += ARBOLES
			else:
				s += estado[j][k]

		nuevo.append(s)

	estado = nuevo
	

nArb = 0
nAlm = 0
for linea in estado:
	nArb += linea.count(ARBOLES)
	nAlm += linea.count(ALMACEN)

print "Solucion:", str(nArb * nAlm)