def converte(h):
        h = h - 12
        return h 

def saída(h, m):
    if h <= 12:
        print(f'{h}:{m} A.M')
    elif h > 12:
        h = converte(h)
        print(f'{h}:{m} P.M')

while True:
    h = int(input('horas:  '))
    m = int(input('minutos:  '))
    saída(h, m)


    

    
    

