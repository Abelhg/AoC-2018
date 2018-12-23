# Advent Of Code: Dia 22 - Segunda parte

import heapq

# Lee entrada
with open('entradaDia22') as f:
	inp = [l.rstrip() for l in f.readlines()]

PROFUNDIDAD = int(inp[0].split()[1])
o = inp[1].split()[1].split(',')
OBJETIVO = (int(o[0]), int(o[1]))

indices_calculados = dict()
niveles_calculados = dict()

heap = [(0, 0, 0, 0)]
visitados = {(0,0): 0}

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

def siguiente(tiempo, (X, Y), equipamiento, calculados):
	vecinos = [(X+1,Y), (X-1,Y), (X,Y+1), (X,Y-1)]
	for v in vecinos:
		if v[0] < 0 or v[1] < 0:
			continue
		if nivelErosion((v[0],v[1])) % 3 == equipamiento:
			continue
		if ((v, equipamiento) in visitados and 
			visitados[(v, equipamiento)] <= tiempo):
			continue
		visitados[(v, equipamiento)] = tiempo
		heapq.heappush(heap, (tiempo, v[0], v[1], equipamiento))

encontrado = False
while not encontrado:
	tiempo, x, y, equipamiento = heapq.heappop(heap)
	if (x,y) == OBJETIVO and equipamiento == 0:
		encontrado = True
	else:
		tiempo += 1
		siguiente(tiempo, (x,y), equipamiento, heap)
		tiempo += 7
		equipamiento = 3 - equipamiento - nivelErosion((x,y)) % 3
		siguiente(tiempo, (x,y), equipamiento, heap)

print "Solucion:", tiempo