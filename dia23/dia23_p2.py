# Advent Of Code: Dia 23 - Segunda parte

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

xs = [x[0][0] for x in nanos] + [0]
ys = [x[0][1] for x in nanos] + [0]
zs = [x[0][2] for x in nanos] + [0]

dist = 1
while dist < max(xs) - min(xs):
	dist *= 2

solucion = None
salir = False
while not salir:
	oCont = 0
	mejor = None
	for x in range(min(xs), max(xs) + 1, dist):
		for y in range(min(ys), max(ys) + 1, dist):
			for z in range(min(zs), max(zs) + 1, dist):
				cont = 0
				for nano in nanos:
					bx, by, bz = nano[0]
					bdist = nano[1]
					calc = manhattan((x,y,z), (bx,by,bz))
					if dist == 1:
						if calc <= bdist:
							cont += 1
					else:
						calc = manhattan((x // dist, y // dist, z // dist),(bx // dist, by // dist, bz // dist))
						if calc - 1 <= bdist // dist:
							cont += 1
				if cont > oCont:
					oCont = cont
					solucion = manhattan((0,0,0), (x,y,z))
					mejor = (x, y, z)
				elif cont == oCont:
					d = manhattan((0,0,0), (x,y,z))
					if solucion is None or d < solucion:
						solucion = d
						mejor = (x, y, z)

	if dist != 1:
		xs = [mejor[0] - dist, mejor[0] + dist]
		ys = [mejor[1] - dist, mejor[1] + dist]
		zs = [mejor[2] - dist, mejor[2] + dist]
		dist = dist // 2
	else:
		salir = True

print "Solucion:", solucion