# Advent Of Code: Dia 23 - Primera parte

def manhattan((X,Y,Z), (X2,Y2,Z2)):
	return abs(X-X2) + abs(Y-Y2) + abs(Z-Z2)

# Lee entrada
with open('entradaDia23') as f:
	inp = [l.rstrip() for l in f.readlines()]

nanos = []
for linea in inp:
	v = linea.split(">, r=")
	s = int(v[1])
	coords = [int(n) for n in v[0][5:].split(',')]
	nanos.append([coords, s])

masFuerte = max(nanos, key=lambda i: i[1])

solucion = 0
for nano in nanos:
	if manhattan(nano[0], masFuerte[0]) <= masFuerte[1]:
		solucion += 1

print "Solucion:", solucion