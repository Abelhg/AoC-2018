# Advent Of Code: Dia 1 - Primera parte

with open('entradaDia1') as f:
	inp = f.readlines()

res = 0
for i in inp:
	res += int(i.split()[0])

print res