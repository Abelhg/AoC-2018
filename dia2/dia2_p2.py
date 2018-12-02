# Advent Of Code: Dia 2 - Segunda parte

# Devuelve una cadena con los caracteres comunes entre 2 cadenas
def comStr(cadena1, cadena2):
	r = ""
	for x in range(len(cadena1)):
		r += cadena1[x] if cadena1[x] == cadena2[x] else ''
	return r

with open('entradaDia2') as f:
	lineas = f.readlines()

res = ""
for i in range(0, len(lineas)):
	for j in range(i+1, len(lineas)):
		dif = comStr(lineas[i], lineas[j]) 

		if len(dif) == len(lineas[i])-1:
			res = dif
			break

print "Resultado:", res