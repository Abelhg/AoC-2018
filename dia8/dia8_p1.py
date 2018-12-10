# Advent Of Code: Dia 8 - Primera parte

def sumaMetas(datos):
	res = 0
	numHijos = int(datos.pop(0))
	numMetas = int(datos.pop(0))
	# Lee los hijos
	while numHijos > 0:
		res += sumaMetas(datos)
		numHijos -= 1
	# Suma los metas
	while numMetas > 0:
		res += int(datos.pop(0))
		numMetas -= 1

	return res

# Lee entrada
with open('entradaDia8') as f:
	inp = f.readlines()

inp = inp[0].split('\n')[0].split(' ')

print "Solucion:", sumaMetas(inp)
