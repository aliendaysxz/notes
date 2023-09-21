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
    print('R$ %.2f - R$ %.2f' % (z[0],z[1]))

print('\nForam processados %d colaboradores' % (len(salarios)))
print('Total gasto com abonos: R$ %.2f' % (sum(abonos)))
print('Valor mínimo pago a %d colaboradores' % (len(a100)))
print('Maior valor de abono pago: R$ %.2f' % (max(abonos)))

    
