# Advent Of Code: Dia 25

import networkx as nx
from ast import literal_eval

def manhattan((X,Y,Z,T), (X2,Y2,Z2,T2)):
	return abs(X2-X) + abs(Y2-Y) + abs(Z2-Z) + abs(T2-T)

# Lee entrada
with open('entradaDia25') as f:
	inp = [l.rstrip() for l in f.readlines()]

grafo = nx.Graph()
for i in range(len(inp)):
	c = literal_eval("(" + inp[i] + ")")
	grafo.add_node(c)
	for j in range(i+1, len(inp)):
		c2 = literal_eval("(" + inp[j] + ")")
		if manhattan(c, c2) <= 3:
			grafo.add_edge(c, c2)

print "Solucion:", nx.number_connected_components(grafo)
