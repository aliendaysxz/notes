import random as r
import operator as op

sist = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
validos = list(range(1,7))
votos = []
d = {}
ps = []

while True:
    v = int(input('Qual o melhor Sistema Operacional para uso em servidores?  '))
    if v < 0 or v > 6:
        print('número inválido!')
        continue
    elif v == 0:
        print('-')
        break
    elif v in validos:
        votos.append(v)

########## 
votos_teste = []
def testes():
    for x in list(range(1,501)):
        v = r.randint(1,6)
        votos_teste.append(v)
    return votos_teste

print(testes())
##########

def contagem (votos):
    for x in votos:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    return d

print(contagem(votos_teste))

def porcent():
    vps = d.values()
    for x in vps:
        p = x*100/total
        ps.append(p)
    return sorted(ps, reverse=True)

total = len(votos_teste)
print(porcent())


cab = """Sistema Operacional     Votos   %
------------------------------------------"""
print(cab)
x = 0
for i in sorted(d, key=d.get,reverse=True):
    tab = '{}       |      {}      |   {}%'. format(sist[i-1], d[i], ps[0+x])
    print(tab)
    x += 1
print('total--------------{}'.format(total))

m = max(d.items(), key=op.itemgetter(1))     
rodape = 'O Sistema Operacional mais votado foi o {}, com {} votos, correspondendo a {}% dos votos.'.format(sist[m[0]-1], m[1], ps[0])
print(rodape)
