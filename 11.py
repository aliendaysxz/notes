meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

def dia(d):
    if int(d)<=9:
        return(d[1])
    else:
        return d

def mes(m):
    tiraZero(m)
    mes = meses[int(m)-1]
    return mes
     
def tiraZero(m):
    if int(m)<=9:
        return (m[1])
    else:
        return m
    

d,m,a = input('data: ').split('/')
print(f'{dia(d)} de {mes(m)} de {a}') 





