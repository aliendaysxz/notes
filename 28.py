d = {'file duplo' : 4.9, 'alcatra' : 5.9, 'picanha' : 6.9}

t = input('tipo:  ')
q = int(input('quantidade(kg):  '))
c = input('cartão?[s/n]  ')

if q>5:
    d[t] += 0.9

total = d[t] * q

if c == 's':
    desconto = total * 0.05
    pagar = total - desconto
    pag = 'cartão'
if c == 'n':
    desconto = 0
    pagar = total
    pag = 'dinheiro'

print("""\nCUPOM FISCAL:\ntipo de carne: {}\nquantidade: {} kg\npreço total: R$ {:.2f}\ntipo de pagamento: {}\ndesconto: R$ {:.2f}\nvalor a pagar: R$ {:.2f}""".format(t,q,total, pag, desconto, pagar))
    
    
    
    
    
    
