import string
import random

atl = string.ascii_uppercase[:5]
salt = []

def converter(lista):
    x = 0
    for salt[x] in lista:
        salt[x] = float(salt[x])
        x += 1
        
def saltos(atl):
    x = 1
    for y in range(1,6):
        i = random.randint(5,9)
        d = random.randint(1,9)
        salt.append(f'{i}.{d}')
        tab = print(f'salto {x}: {i}.{d}')
        x+=1
    return tab

def result_final(atl):
    a = print('resultado final:')
    b = print('atleta: {}'.format(atl))
    
    
c = 0
cc = 1
for a in atl:
    print('atleta: {}'.format(a))
    saltos(a)
    converter(salt)
    result_final(a)
    media = sum(salt[0+(5*c):(5*cc)])/5
    print(f'saltos: {salt[0+(5*c):(5*cc)]}')
    print(f'media dos saltos: {media: .2f}\n')
    c += 1
    cc += 1

