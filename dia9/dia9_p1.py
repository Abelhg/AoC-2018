# Advent Of Code: Dia 9 - Primera parte
from collections import deque

# Lee entrada
with open('entradaDia9') as f:
	inp = f.readlines()

inp = inp[0].split('\n')[0].split(' ')
numJugadores = int(inp[0])
ultValor = int(inp[6])
puntos = numJugadores * [0]
tablero = deque([0])
jugActual = 1
indActual = 0
for valor in range(1, ultValor+1):
	if valor % 23 == 0:
		# Caso especial multiplo de 23
		tablero.rotate(7)
		puntos[jugActual-1] += valor + tablero.pop()
		tablero.rotate(-1)
	else:
		# Caso normal
		tablero.rotate(-1)
		tablero.append(valor)
		
	jugActual += 1
	if jugActual > numJugadores:
		jugActual = 1

# La solucion es la mayor puntuacion
print "Solucion:", max(puntos)