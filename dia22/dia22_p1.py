# Advent Of Code: Dia 22 - Primera parte


# Lee entrada
with open('entradaDia22') as f:
	inp = [l.rstrip() for l in f.readlines()]

PROFUNDIDAD = int(inp[0].split()[1])
o = inp[1].split()[1].split(',')
OBJETIVO = (int(o[0]), int(o[1]))

indices_calculados = dict()
niveles_calculados = dict()

def indiceGeologico(posicion):
	if posicion in indices_calculados:
		return indices_calculados[posicion]

	if posicion == (0,0) or posicion == OBJETIVO:
		ret = 0
	elif posicion[0] == 0:
		ret = 48271 * posicion[1]
	elif posicion[1] == 0:
		ret = 16807 * posicion[0]
	else:
		n1 = nivelErosion((posicion[0] - 1, posicion[1]))
		n2 = nivelErosion((posicion[0], posicion[1]-1))
		ret = n1 * n2

	indices_calculados[posicion] = ret
	return ret

def nivelErosion(posicion):
	if posicion in niveles_calculados:
		return niveles_calculados[posicion]
	return (indiceGeologico(posicion) + PROFUNDIDAD) % 20183

solucion = 0
for i in range(OBJETIVO[1]+1):
	for j in range(OBJETIVO[0]+1):
		solucion += nivelErosion((j,i)) % 3

print "Solucion:", solucion