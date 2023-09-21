import random as r
import operator as op

votos_teste = []
def testes():
    for x in list(range(1,101)):
        v = r.randint(1,23)
        votos_teste.append(v)
    return votos_teste

##############################################

vot = open('votação.txt', 'w')

votos = []
ps = []
validos = list(range(1,24))

while True:
    v = input('nº do jogador (0=fim):  ')
    if int(v) < 0 or int(v) > 23:
        print('número inválido!')
        continue
    elif int(v) == 0:
        print('-')
        break
    elif int(v) in validos:
        votos.append(int(v))
        
def contagem(v):
    global d
    d = dict()
    for x in v:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    return d

def porcent(votosCada, T):
    for valor in votosCada:
        p = valor*100/total
        ps.append(p)
    return sorted(ps, reverse=True)

testes()

print(votos_teste)

print('\n{}\n'.format(contagem(votos_teste)))

total = len(votos_teste)
print('total de votos válidos: {}\n'.format(total))

vpj = d.values()
ps = porcent(vpj, total)
print('{}\n'.format(ps))


cabeçalho = """Resultado da votação:\n
Foram computados {} votos.
Jogador  |   Votos   |    % de Votos   |""".format(total)

x=0
vot.write(cabeçalho)
for i in sorted(d, key=d.get, reverse=True):
    tab = '{}       |   {}       |    {}        |'.format(i, d[i], ps[0+x])
    vot.write('\n{}\n'.format(tab))
    x += 1
    if x==5:
        break

m = max(d.items(), key=op.itemgetter(1))
vot.write('\nO melhor jogador foi o número {}, com {} votos, correspondendo a {}% do total de votos.'.format(m[0],m[1], ps[0]))

vot.close()
