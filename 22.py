import random as r
import operator as op

tipo = ['necessita da esfera','necessita de limpeza','necessita troca do cabo ou conector','quebrado ou inutilizado']
defeitos = []
ps = []

print('Defeitos:\n1 - Necessita de Esfera\n2 - Necessita de limpeza\n3 - Necessita troca de cabo ou conector\n4 - Quebrado ou inutilizado')
valido = list(range(1,5))
while True:
    defeito = int(input('tipo de defeito:  '))
    if defeito == 0:
        print('-')
        break
    if defeito not in valido:
        print('valor inválido!')
        continue
    elif defeito in valido:
        defeitos.append(defeito)
print(defeitos)

dic = {}
def contagem():
    for d in defeitos:
        if d not in dic:
            dic[d] = 1
        if d in dic:
            dic[d] += 1
    return dic
print(contagem())

def porcent():
    for d in dic.items():
        p = d[1]*100/len(defeitos)
        ps.append(p)
    return ps
porcent()
ps = sorted(ps, reverse=True)
print(ps)

print('\nQuantidade de mouses: {}'.format(len(defeitos)))

print('Situação - Quantidade - Percentual')
k = sorted(dic.items(), key=op.itemgetter(1), reverse=True)
x = 0
for i in k:
    print('{}- {}   |   {}   |   {:.2f}%'.format(1+x, tipo[i[0]-1], i[1], ps[0+x]))
    x += 1
