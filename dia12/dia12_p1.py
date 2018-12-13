# Advent Of Code: Dia 12 - Primera parte

# Lee entrada
with open('entradaDia12') as f:
	inp = f.readlines()

minp = 0
plantas = inp[0][15:].rstrip()

transf = {}
for i in range(2, len(inp)):
	s = inp[i].rstrip()
	transf[s[:5]] = s[9:]

NUMIT = 20
for i in range(NUMIT):
	pri = plantas[:6]
	if '#' in pri:
		# Se colocan . al principio
		plantas = "....." + plantas
		minp += 5
	sec = plantas[len(plantas)-5:]
	if '#' in sec:
		# Se colocan . al final
		plantas += "....."
	res = ".."
	for j in range(len(plantas)-4):
		cad = plantas[j:j+5]
		if cad in transf.keys():
			# Se transforma
			res += transf[cad]
		else:
			# Se pone .
			res += "."
	res += ".."
	plantas = res

solucion = 0
for i in range(len(plantas)):
	if plantas[i] == '#':
		solucion += (i-minp)

print "Solucion:", solucion