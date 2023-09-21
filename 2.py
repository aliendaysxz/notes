def ex_2(n):
    for x in range(1,n+1):
        print(list(range(1,x+1)))

#ou
        
def imprimeLinha(n):
    for x in range(1, n+1):
        print((f' {x} '), end = '')
    print()
    
def imprimeSeq(n):
    for n in range(1,n+1):
        imprimeLinha(n)
    
