# Advent Of Code: Dia 20 - Segunda parte

import networkx as nx

# Lee entrada
with open('entradaDia20') as f:
	direcciones = f.read()[1:-1]

mapa = nx.Graph()
actual = (0, 0) # x y
guardadas = []
desplazamientos = {'N': (0,-1), 'E': (1,0), 'W': (-1, 0), 'S': (0,1)}

for d in direcciones:
	if d in 'NEWS':
		desp = desplazamientos[d]
		mapa.add_edge( (actual[0], actual[1]), (actual[0]+desp[0], actual[1] + desp[1]) )
		actual = (actual[0]+desp[0], actual[1] + desp[1])
	elif d == '|':
		actual = guardadas[-1]
	elif d == '(':
		guardadas.append(list(actual))
	elif d == ')':
		actual = guardadas.pop()

longs = nx.algorithms.shortest_path_length(mapa, (0,0)).values()
print "Solucion:", sum(1 for l in longs if l >= 1000)