# Advent Of Code: Dia 4 - Primera parte

# Lee entrada
with open('entradaDia4') as f:
	inp = f.readlines()

# Formato datos: [AAAA-MM-DD HH:MM:SS]	"Guard #ID begins shift"
#										"falls asleep"
#										"wakes up"

inp.sort() # Ordena cronologicamente

# Coloca delante de cada cadena, el guardia al que se refiere
ID_GUARDIA = "#"
for i in range(len(inp)):
	linea = inp[i].split('\n')[0]
	if "Guard" in linea:
		# Nuevo guardia
		alm = linea.find('#')
		spc = linea.find(' ', alm)
		ID_GUARDIA = linea[alm:spc]

	inp[i] = ID_GUARDIA + " " + linea

inp.sort() # Ordena por ID

# Busca el guardia que mas duerme
ID_GUARDIA = "#"
TIEMPO = 0
INICIO = 0
FIN = 0
ID = "#"
tpo = 0
ini = 0
i = 0
for linea in inp:
	ID_N = linea[:linea.find(' ')]
	if ID_N != ID:
		if tpo > TIEMPO:
			# Guardia que ha dormido mas que los anteriores
			ID_GUARDIA = ID
			TIEMPO = tpo
			INICIO = ini
			FIN = i
		ID = ID_N
		tpo = 0
		ini = i
	elif "falls" in linea:
		# Comienza a dormir
		z = linea.find(':')
		MIN = int(linea[z+1:z+3])
	elif "wakes" in linea:
		# Despierta
		z = linea.find(':')
		M = int(linea[z+1:z+3])
		tpo += (M - MIN)
	i += 1

TPOS_GUARDIA = inp[INICIO:FIN]
print "El guardia que mas duerme es", ID_GUARDIA, "con", TIEMPO,"minutos."

TABLA = []
FECHAS = []
INICIAL = 60*['.']
a_meter = list(INICIAL)
for linea in TPOS_GUARDIA:
	z = linea.find(' ')
	fecha = linea[z+7:z+12] # Fecha
	if fecha not in FECHAS and "23:" not in linea:
		FECHAS.append(fecha)
		TABLA.append(a_meter)	# La primera es inservible
		a_meter = list(INICIAL)
	if "falls" in linea:
		min_dorm = int(linea[z+16:z+18])
	elif "wakes" in linea:
		min_desp = int(linea[z+16:z+18])
		# Rellena almohadillas entre ambos minutos
		for i in range(min_dorm, min_desp):
			a_meter[i] = '#'

TABLA = TABLA[1:]

# Salida visual
print "\nGuardia", ID_GUARDIA
print "FECHA\tMinuto"
s = ""
for i in range(60):
	s += str(i/10)
print "\t" + s
s = ""
for i in range(60):
	s += str(i%10)
print "\t" + s

for i in range(len(TABLA)):
	s = ""
	for col in TABLA[i]:
		s += col
	print FECHAS[i] + '\t' + s

# Obtiene el minuto mas frecuente
MIN = 0
CNT = 0
for i in range(60):
	c = [fil[i] for fil in TABLA].count('#')
	if c > CNT:
		CNT = c
		MIN = i

print "Solucion:", MIN