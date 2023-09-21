from random import randint

def linhas(l):
    linha = '+ ' + '- '*l + '+'
    return linha

def colunas(c):
    coluna = '| '+ ' '*l*2 + '|'
    n=1
    while n<c:
        print(coluna)
        n+=1
    return coluna

def ret():
    print(linhas(l))
    print(colunas(c))
    print(linhas(l))

print('nota: para valores fora dos limites, l e c serão sorteados')
l = int(input('nº de linhas(1-20):  '))
if l not in range(1,20):
    l = randint(1,20)
else:
    l=l
c = int(input('nº de colunas(1-20):  '))
if c not in range(1,20):
    c = randint(1,20)
else:
    c=c

ret()





    

    
