salarios = []
abonos = []
a100 = []

while True:
    s = int(input('salario:  '))
    salarios.append(s)
    if s == 0:
        print('-')
        salarios.remove(0)
        break

print(salarios)

def abono():
    for s in salarios:
        a = s*0.2
        if s*0.2 < 100:
            a = 100
            a100.append(a)
        abonos.append(a)
    return abonos
print(abono())

print('\nProjeção de Gastos com Abono')
print('============================')

lista = list(zip(salarios,abonos))
print('salário - abono')

for z in lista:
    print('R$ {} - R$ {}'.format(z[0],z[1]))

print('\nForam processados {} colaboradores'.format(len(salarios)))
print('Total gasto com abonos: R$ {}'.format(sum(abonos)))
print('Valor mínimo pago a {} colaboradores'.format(len(a100)))
print('Maior valor de abono pago: R$ {}'.format(max(abonos)))

    
