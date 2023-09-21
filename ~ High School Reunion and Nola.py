import numpy as np

d = 185 - np.arange(5*7)/5
print(d)

sc = d[6:-1].reshape(4,7)
print(sc)

r = np.array(sc[0:4, [7//2]])
r2 = np.insert(r,0,sum(d[0:6])/6)
r3 = np.append(r2, d[-1])
print('MÉDIAS POR SEM =', r3)

print('--------')

sab = d[5::7]
print(sab)
dom = d[6::7]
print(dom)
soma = sab + dom
print('MÉDIA POR FINAL DE SEMANA =', soma/2)
