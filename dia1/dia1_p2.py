# Advent Of Code: Dia 1 - Segunda parte

with open('entradaDia1') as f:
	inp = f.readlines()

calculadas = []

res = 0
repe = 0
found = False
while not found:
	for i in inp:
		res += int(i.split()[0])
		if res in calculadas:
			found = True
			repe = res
			break
		else:
			calculadas.append(res)

print repe
