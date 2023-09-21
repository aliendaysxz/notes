import random as r
import operator as op
mod = ['fusca','gol','uno','vectra','peugeout']
kml = []
lmilkm = []
RSlmilkm = []
d = {}
for x in list(range(1,6)):
    k = r.randint(5,15)
    kml.append(k)
    d[mod[x-1]] = k

print('MODELOS: {}\nKM POR L: {}\n\n{}'.format(mod,kml,d))

def milq():
    for x in kml:
        lmilkm.append(f'{1000/x: .2f}')
        RSlmilkm.append(f'{(1000/x)*2.25:.2f}')
    return print(f'{lmilkm}\n{RSlmilkm}')

milq()

c = 0
for m in mod:
    print('\nveículo {}\nnome: {}\nkm por litro: {}\n'.format(1+c,mod[0+c],kml[0+c]))
    c += 1

print('\nRELATORIO FINAL')
for x in list(range(1,6)):
    print('{}- {} - {} - {} litros - R$ {}'. format(x, mod[x-1], kml[x-1], lmilkm[x-1], RSlmilkm[x-1]))
    
m = max(d.items(), key=op.itemgetter(1))
print('O menor consumo é do {}.'.format(m[0].upper()))
    
        
