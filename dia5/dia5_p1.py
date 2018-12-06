# Advent Of Code: Dia 5 - Primera parte

# Reacciona un polimero: borra ocurrencias tipo Aa/aA
def reacPolimero(cadena):
	i = 0
	salir = False
	while not salir:
		if cadena[i].lower() == cadena[i+1].lower():
			# Mismo caracter
			if cadena[i] != cadena[i+1]:
				# Distinta capitalizacion -> se borran
				cadena = cadena[:i] + cadena[i+2:] 
				# Para comprobar la anterior
				i -= 2
		i += 1
		if i == len(cadena)-2:
			salir = True
	return cadena

# Lee entrada
with open('entradaDia5') as f:
	inp = f.readlines()

inp = inp[0]

print "Solucion:", len(reacPolimero(inp))-1