import random
range_id = list(range(10,16))
range_alt = list(range(50, 81))
alunos = list(range(1,31))
idades = []
alturas = []
print(alunos)
print('\n')
for x in alunos:
    idades.append(random.sample(range_id, 1)[0])
print(idades)
print('\n')

for x in alunos:
    alt = '1.{}'.format(random.sample(range_alt, 1)[0])
    alturas.append(float(alt))
print(alturas)
print('\n')

media = sum(alturas)/30
print('{: .2f}'.format(media))
print('\n')

pares = list(zip(idades, alturas))
resp = 0
for y in pares:
    if y[0] == 13 and y[1] < media:
        resp = resp + 1
    else:
        resp = resp

print(resp)


