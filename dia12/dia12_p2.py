# Advent Of Code: Dia 12 - Segunda parte

# Lee entrada
with open('entradaDia12') as f:
	inp = f.readlines()

minp = 500
plantas = minp*['.'] + list(inp[0][15:].rstrip()) + minp*['.']

transf = dict()
for i in range(2, len(inp)):
	s = inp[i].rstrip()
	transf[s[:5]] = s[9:]

sumaPrev = 0
# Al final acaba estabilizandose la diferencia entre iteraciones
NUMIT = 100
for i in range(NUMIT):
	nPlantas = 2*['.']
	for j in range(2, len(plantas)-2):
		cad = "".join(plantas[j-2:j+3])
		if cad in transf.keys():
			# Se transforma
			nPlantas.append(transf[cad])
		else:
			# Se pone .
			nPlantas.append(".")
	nPlantas += 2*['.']
	plantas = nPlantas

	suma = 0
	for k in range(len(plantas)):
		if plantas[k] == '#':
			suma += (k-minp)

	diferencia = suma - sumaPrev
	sumaPrev = suma

solucion = (50000000000 - NUMIT) * diferencia + suma
print "Solucion:", solucion