import random
import string

def prim(n):
    for x in range(n):
        print(x+1)
    return
prim(5)

def prim2(n):
    lista = []
    for x in range(n):
        lista.append(x+1)
    return print(lista)
prim2(5)

print('\n')

def seg(n):
    lista = []
    for x in range(n):
        lista.append(x+1)
    lista.reverse()
    return print(lista)
seg(10)

def seg2(n):
    lista = []
    for x in range(n):
        lista.append(x+1)
    return print(lista[::-1])
seg2(10)

print('\n')

def terc():
    x = list(range(1,10))
    notas = random.sample(x,4)
    a = print('notas: ', notas)
    b = print('média: ',(sum(notas)/4))
    return a,b
terc()

print('\n')

def quart():
    cons = []
    l = list(string.ascii_letters)
    n = list(range(1,10))
    c = l + n
    random.shuffle(c)
    vetor10 = random.sample(c,10)
    x = 0
    for caract in vetor10:
        if caract not in n and caract not in 'aeiouAEIOU':
            x += 1
            cons.append(caract)
        else:
            x = x
    a = print('consoantes:  ', cons)
    b = print('nº de caracteres: ',x)
    return a,b
quart()

print('\n')

def quint():
    p = []
    i = []
    numeros = list(range(0, 101))
    vetor20 = random.sample(numeros, 20)
    for n in vetor20:
        if n%2==0:
            p.append(n)
        elif n%2!=0:
            i.append(n)
    a = print('pares: ', sorted(p))
    b = print('impares: ', sorted(i))
    return p,i
quint()

print('\n')
