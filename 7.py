valores = []
q = 0

def valorPagamento(valor, dias):
    if dias == 0:
        return valor
    elif dias >= 1:
        return valor + (valor*0.03) + (valor*0.001*dias)
    valores.append(valor)

def relatorio(q):
    a = f'número de prestações pagas: {q}'
    b = f'total pago: {sum(valores)}'
    return a, b
    
while True:
    valor = int(input('valor da prestação:  '))

    if valor == 0:
        print(relatorio(q))
        break

    dias = int(input('dias em atraso:  '))

    valor2 = valorPagamento(valor, dias)
    print(valor2)
    valores.append(valor2)

    q = q + 1
    
    
   
    
