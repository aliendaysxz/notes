import random

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'dez', 'out']
n = list(range(25,35))
medias = []
for x in list(range(1,13)):
    medias.append(random.randint(20,40))
media_anual = sum(medias)/12
print(medias)
print('{: .2f}'.format(media_anual))

dic = {}
c = 0
for m in meses:
    dic[meses[0+c]] = medias[0+c]
    c += 1
    
print(dic)

for m in meses:
    if dic[m] > media_anual:
        print(m)
    else:
        print('-')

print('\n..........\n')

listazip = list(zip(meses, medias))
for k in listazip:
    if k[1] > media_anual:
        print(k[0])
    else:
        print('-')


    
