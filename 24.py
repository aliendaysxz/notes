import random as r
d = {}
vetor = []

def dado():
    for e in list(range(1,101)):
        v = r.randint(1,6)
        vetor.append(v)
    return vetor

print(dado())

def contagem():
    for x in vetor:
        if x not in d:
            d[x] = 1
        if x in d:
            d[x] += 1
    return d

print(contagem())

for i in sorted(d.items()):
    print('\nnº {} - {} vezes'.format(i[0], i[1]))
