import random

vendas = random.sample(list(range(1000, 8000)), 10)
sal = []

def salario(venda):
    return (venda*0.09)+200


for v in vendas:
    s = salario(v)
    sal.append(int(s))
print(sal)
    


