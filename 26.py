t = input('tipo (A ou G): ')
q = int(input('litros: '))
 
if t == 'A':
    litro =  1.9
    if q <= 20:
        valor = litro * 0.97
    elif q > 20:
        valor = litro * 0.95
        
elif t == 'G':
    litro =  2.5
    if q <= 20:
        valor = litro * 0.96
    elif q > 20:
        valor = litro * 0.94

total = valor * q
print('total a pagar: R${:.2f}'.format(total))
        
