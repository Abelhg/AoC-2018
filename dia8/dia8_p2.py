# Advent Of Code: Dia 8 - Segunda parte

def valorNodo(datos):
	res = 0
	numHijos = int(datos.pop(0))
	numMetas = int(datos.pop(0))

	if numHijos == 0:
		# El valor del nodo es la suma de metas
		while numMetas > 0:
			res += int(datos.pop(0))
			numMetas -= 1
	else:
		# El valor del nodo depende de los hijos
		hijos = []
		while numHijos > 0:
			hijos.append(valorNodo(datos))
			numHijos -= 1

		# Los metas son indices de hijos
		while numMetas > 0:
			ind = int(datos.pop(0))-1 # Indices > 0
			if ind < len(hijos):
				res += hijos[ind]
			numMetas -= 1

	return res

# Lee entrada
with open('entradaDia8') as f:
	inp = f.readlines()

inp = inp[0].split('\n')[0].split(' ')

print "Solucion:", valorNodo(inp)