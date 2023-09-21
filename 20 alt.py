print('Digite 0 para encerrar o programa')
salarios = [] 
while True:
    salario = float(input('Salário: '))
    if salario == 0:
        break
    salarios.append(salario)

print('\nProjeção de Gastos com Abono')
print('============================')

print('Salário - Abono')
abonos = 0
minimo = 0
maior = 0
for s in salarios:
    abono = (s * 20) / 100
    if abono < 100:
        abono = 100
        minimo += 1
    if abono > maior:
        maior = abono
    abonos += abono
    print('R$ %.2f - R$ %.2f' % (s, abono))

print('Foram processados %d colaboradores' % (len(salarios)))
print('Total gasto com abonos: R$ %.2f' % abonos)
print('Valor mínimo pago a %d colaboradores' % minimo)
print('Maior valor de abono pago: R$ %.2f' % maior)
