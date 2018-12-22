# Advent Of Code: Dia 21 - Primera parte

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

# Lee entrada
with open('entradaDia21') as f:
	inp = [l.rstrip() for l in f.readlines()]

ip_r = int(inp[0].split()[1])
programa = inp[1:]
REGISTROS = [0, 0, 0, 0, 0, 0]
while REGISTROS[ip_r] != 28:
	instr = programa[REGISTROS[ip_r]].split()
	REGISTROS = locals()[instr[0]](REGISTROS, instr[1:])
	REGISTROS[ip_r] += 1

print "Solucion:", REGISTROS[4]