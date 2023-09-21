import random 
import string

a = string.ascii_uppercase
r = list(range(1,11))
d = {}
for l in a[:15]:
    d[l] = random.sample(r,7)

def result():
    for x in d:
        print('\nAtleta: {}'.format(x))
        melhor = max(d[x])
        print('Melhor nota: {}'.format(melhor))
        d[x].remove(melhor)
        pior = min(d[x])
        print('Pior nota: {}'.format(pior))
        d[x].remove(pior)
        media = sum(d[x])/5
        print('Média: {:.2f}'.format(media))


print('--------RESULTADO FINAL--------')
result()


    
