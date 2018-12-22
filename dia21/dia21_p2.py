# Advent Of Code: Dia 21 - Segunda parte

b = 0
vistos = set()
ultima = 0

salir = False
while not salir:
	a = b | 65536
	b = 14464005

	while True:
		b = ((((a & 255) + b) & 16777215) * 65899) & 16777215

		if a < 256:
			if b not in vistos:
				vistos.add(b)
				ultima = b
			else:
				salir = True
			
			break
		else:
			a = int(a / 256)

print "Solucion:", ultima