# Advent Of Code: Dia 4 - Segunda parte

# Devuelve la tabla de los datos de un guardia
def tablaGuardia(TPOS_GUARDIA):
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

	return TABLA[1:]

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

# Genera la tabla de cada guardia
TABLAS_GUARDIAS = []
IDS_GUARDIAS = []
ID = "#"
ini = 0
i = 0
for linea in inp:
	ID_N = linea[:linea.find(' ')]
	if ID_N != ID:
		# Guardia diferente
		IDS_GUARDIAS.append(ID)
		TABLAS_GUARDIAS.append(tablaGuardia(inp[ini:i]))
		ID = ID_N
		ini = i
	i += 1

# La primera es vacia
IDS_GUARDIAS = IDS_GUARDIAS[1:]
TABLAS_GUARDIAS = TABLAS_GUARDIAS[1:]

# Recorre cada minuto y averigua que guardia lo duerme mas y cuantas veces
ID_SOLUCION = "#"
CNT_SOLUCION = 0
MIN_SOLUCION = 0
for i in range(60):
	ID = "#"
	cnt = 0
	for j in range(len(TABLAS_GUARDIAS)):
		c = [fil[i] for fil in TABLAS_GUARDIAS[j]].count('#')
		if c > cnt:
			cnt = c
			ID = IDS_GUARDIAS[j]
	if cnt > CNT_SOLUCION:
		ID_SOLUCION = ID
		CNT_SOLUCION = cnt
		MIN_SOLUCION = i

print "Solucion:", ID_SOLUCION, "- Minuto", str(MIN_SOLUCION), "-", str(CNT_SOLUCION), "veces"