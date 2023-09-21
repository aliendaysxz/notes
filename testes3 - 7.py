import random

n = list(range(0,101))
v = sorted(random.sample(n, 5))
    
def soma(vetor):
    return sum(vetor)

def mult(vetor):
    a = 1
    for x in vetor:
        a = a*x
    return a

def resposta():
    s = soma(v)
    m = mult(v)
    return print(f'números = {v}\nsoma = {s}\nmultiplicação = {m}')

resposta()



    
