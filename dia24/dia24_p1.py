# Advent Of Code: Dia 24 - Primera parte

class Grupo:
	def __init__(self, ID, ejercito, nUnidades, vida, ataque, tipo, iniciativa, debilidades, inmunidades):
		self.ID = ID
		self.ejercito = ejercito
		self.nUnidades = nUnidades
		self.vida = vida
		self.ataque = ataque
		self.tipo = tipo
		self.iniciativa = iniciativa
		self.debilidades = debilidades
		self.inmunidades = inmunidades
		self.objetivo = None

	def poderEfectivo(self):
		return self.nUnidades * self.ataque

def generaGrupo(ID, cadena, ejercito):
	vals = cadena.split()
	num = int(vals[0])
	vid = int(vals[4])
	ata = int(vals[-6])
	tip = vals[-5]
	ini = int(vals[-1])
	# Inmunidades
	inmus = []
	iW = cadena.find("immune to")
	if iW != -1:
		iW += 10
		s = cadena.find(";", iW)
		s2 = cadena.find(")", iW)
		if s != -1:
			iWF = s
		else:
			iWF = s2
		inmus = cadena[iW:iWF].split(', ')
	# Debilidades
	debis = []
	dW = cadena.find("weak to")
	if dW != -1:
		dW += 8
		s = cadena.find(";", dW)
		s2 = cadena.find(")", dW)
		if s != -1:
			dWF = s
		else:
			dWF = s2
		debis = cadena[dW:dWF].split(', ')

	return Grupo(ID, ejercito, num, vid, ata, tip, ini, debis, inmus)

def calcularDanio(atacante, defensor):
	d = atacante.poderEfectivo()
	if atacante.tipo in defensor.inmunidades:
		d = 0
	elif atacante.tipo in defensor.debilidades:
		d *= 2
	return d

# Lee entrada
with open('entradaDia24') as f:
	inp = [l.rstrip() for l in f.readlines()]

# Genera los grupos desde entrada
sep = inp.index('')
inmu = inp[1:sep]
infe = inp[sep+2:]

GRUPOS = []
cont = 1
for i in inmu:
	GRUPOS.append(generaGrupo("INM-"+str(cont),i, "INM"))
	cont += 1

cont = 1
for i in infe:
	GRUPOS.append(generaGrupo("INF-"+str(cont),i, "INF"))
	cont += 1

# Bucle de rondas
while True:
	nInf = sum(i.ejercito == "INF" for i in GRUPOS)
	nInm = sum(i.ejercito == "INM" for i in GRUPOS)

	gINF = [g for g in GRUPOS if g.ejercito == "INF"]
	gINM = [g for g in GRUPOS if g.ejercito == "INM"]

	if nInm == 0 or nInf == 0:
		break

	# FASE 1: SELECCION DE OBJETIVO	
	# Ordena grupos por orden decreciente de poder e iniciativa
	gINF.sort(key=lambda g: (g.poderEfectivo(), g.iniciativa), reverse=True)
	gINM.sort(key=lambda g: (g.poderEfectivo(), g.iniciativa), reverse=True)
	flagsINF = len(gINF) * [False]
	flagsINM = len(gINM) * [False]

	ataques = [(gINF, gINM, flagsINM), (gINM, gINF, flagsINF)]

	# Primero ataca infeccion, luego inmunitario
	for a in ataques:
		for grupo in a[0]:
			grupo.objetivo = None
			dMayor = -1
			for j in range(len(a[1])):
				g = a[1][j]
				# Selecciona grupo enemigo que no este seleccionado ya
				if not a[2][j]:
					# Comprueba si ataca mejor a este grupo
					d = calcularDanio(grupo, g)
					p1 = g.poderEfectivo()
					try:
						p2 = grupo.objetivo.poderEfectivo()
					except:
						pass
					if (d > dMayor) or ( (d == dMayor) and ( (p1 > p2) or (p1 == p2 and g.iniciativa > grupo.objetivo.iniciativa) ) ):
						a[2][j] = True
						try:
							a[2][a[1].index(grupo.objetivo)] = False
						except:
							pass
						dMayor = d
						grupo.objetivo = g
	
	# FASE 2: ATAQUE
	# Ordena grupos por iniciativa
	GRUPOS.sort(key=lambda g: g.iniciativa, reverse=True)
	i = 0
	while i < len(GRUPOS):
		grupo = GRUPOS[i]
		if grupo.objetivo != None:
			d = calcularDanio(grupo, grupo.objetivo)
			# Ataca
			grupo.objetivo.nUnidades -= int(float(d) / grupo.objetivo.vida)
			if grupo.objetivo.nUnidades <= 0:
				# Se elimina grupo
				indice = GRUPOS.index(grupo.objetivo)
				GRUPOS.remove(grupo.objetivo)
				if indice < i:
					i -= 1
		i += 1	

print "Solucion:", sum(g.nUnidades for g in GRUPOS)