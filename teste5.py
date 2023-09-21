import random

lista = []
lista2 = []
def q9():
    for x in list(range(1,11)):
        lista.append(random.randint(1,101))
    return sorted(lista)

def q9_2():
    lista = q9()
    for y in sorted(lista):
        y = y**2
        lista2.append(y)
    soma = sum(lista2)
    return lista2, soma

lista2,soma = q9_2()

print('{}\n{}\n{}'.format(lista, lista2, soma))

print('\n')

def q10(l1, l2):
    l3 = []
    lz = list(zip(l1,l2))
    for n in lz:
        l3.append(n[0])
        l3.append(n[1])
    return print(l3)

q10(lista, lista2)

def q10_2(l1,l2):
    return print(list(zip(l1,l2)))

q10_2(lista, lista2)


print('\n')


lista3 = list(range(0,10))
lista4 = list(range(0,10))
lista5 = list(range(0,10))

def q11(l3,l4,l5):
    l6 = []
    x = 0
    for x in l3:
        l6.append(l3[0+x])
        l6.append(l4[0+x])
        l6.append(l5[0+x])
        x = x + 1
    return print(l6)
q11(lista3, lista4, lista5)

def q11_2(l3,l4,l5):
    for a,b,c in list(zip(l3,l4,l5)):
        print(a, b, c)
q11_2(lista3, lista4, lista5)







    
    
                  
