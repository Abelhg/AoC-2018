# Advent Of Code: Dia 16 - Primera parte

import ast

# Definicion de opcodes.
def addr(registros, cadena):
	registros[int(cadena[2])] = registros[int(cadena[0])] + registros[int(cadena[1])]
	return registros

def addi(registros, cadena):
	registros[int(cadena[2])] = registros[int(cadena[0])] + int(cadena[1])
	return registros

def mulr(registros, cadena):
	registros[int(cadena[2])] = registros[int(cadena[0])] * registros[int(cadena[1])]
	return registros

def muli(registros, cadena):
	registros[int(cadena[2])] = registros[int(cadena[0])] * int(cadena[1])
	return registros

def banr(registros, cadena):
	registros[int(cadena[2])] = registros[int(cadena[0])] & registros[int(cadena[1])]
	return registros

def bani(registros, cadena):
	registros[int(cadena[2])] = registros[int(cadena[0])] & int(cadena[1])
	return registros

def borr(registros, cadena):
	registros[int(cadena[2])] = registros[int(cadena[0])] | registros[int(cadena[1])]
	return registros

def bori(registros, cadena):
	registros[int(cadena[2])] = registros[int(cadena[0])] | int(cadena[1])
	return registros

def setr(registros, cadena):
	registros[int(cadena[2])] = registros[int(cadena[0])]
	return registros

def seti(registros, cadena):
	registros[int(cadena[2])] = int(cadena[0])
	return registros

def gtir(registros, cadena):
	registros[int(cadena[2])] = 1 if int(cadena[0]) > registros[int(cadena[1])] else 0
	return registros

def gtri(registros, cadena):
	registros[int(cadena[2])] = 1 if registros[int(cadena[0])] > int(cadena[1]) else 0
	return registros

def gtrr(registros, cadena):
	registros[int(cadena[2])] = 1 if registros[int(cadena[0])] > registros[int(cadena[1])] else 0
	return registros

def eqir(registros, cadena):
	registros[int(cadena[2])] = 1 if int(cadena[0]) == registros[int(cadena[1])] else 0
	return registros

def eqri(registros, cadena):
	registros[int(cadena[2])] = 1 if registros[int(cadena[0])] == int(cadena[1]) else 0
	return registros

def eqrr(registros, cadena):
	registros[int(cadena[2])] = 1 if registros[int(cadena[0])] == registros[int(cadena[1])] else 0
	return registros

opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

# Lee entrada
with open('entradaDia16') as f:
	inp = f.read()

inp = inp.split('\n\n\n\n')
ejemplos = inp[0].split('\n')

solucion = 0
i = 0
while i < len(ejemplos):
	linea = ejemplos[i]
	antes = ast.literal_eval(linea[linea.find('['):])
	linea = ejemplos[i+1]
	opcode = linea[:linea.find(' ')]
	cadena = linea[linea.find(' ')+1:].split(' ')
	linea = ejemplos[i+2]
	despues = ast.literal_eval(linea[linea.find('['):])
	# Comprueba que opcodes corresponden
	posibles = 0
	for op in opcodes:
		if op(list(antes), cadena) == despues:
			posibles += 1

	if posibles > 2:
		solucion += 1

	i += 4

print "Solucion:", solucion