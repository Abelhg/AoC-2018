# Advent Of Code: Dia 2 - Primera parte

# Devuelve tupla de dos enteros, 0 o 1 dependiendo de:
#  Primer valor: 1 si la cadena contiene exactamente 2 ocurrencias 
#	de una letra cualquiera, 0 si no.
#  Segundo valor: 1 si la cadena contiene exactamente 3 ocurrencias 
#	de una letra cualquiera, 0 si no.
def fun(cadena):
	res1 = 0
	res2 = 0
	# Primer valor
	for letra in cadena:
		if cadena.count(letra) == 2:
			res1 = 1
			break 		# No busca mas
	# Segundo valor
	for letra in cadena:
		if cadena.count(letra) == 3:
			res2 = 1
			break 		# No busca mas

	return (res1, res2)



with open('entradaDia2') as f:
	lineas = f.readlines()

ocurs2 = 0
ocurs3 = 0

for linea in lineas:
	(v1, v2) = fun(linea)
	ocurs2 += v1
	ocurs3 += v2

print "Resultado:", ocurs2, "*", ocurs3,"=", (ocurs2*ocurs3)