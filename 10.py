import random

def jogada():
    d1 = random.randint(1,6)
    print('dado 1: {}'.format(d1))
    d2 = random.randint(1,6)
    print('dado 2: {}'.format(d2))
    soma = d1 + d2
    return soma

def primeira_jogada():
    soma = jogada()
    global venceu
    venceu = '\nNATURAL!!\nvocê ganhou.\n'
    global perdeu
    perdeu = '\ncraps =(\nperdesse.\n'
    if soma in [7,11]:
        return venceu
    elif soma in [2,3,12]:
        return perdeu
    elif soma in [4,5,6,8,9,10]:
        global ponto
        ponto = soma
        return '{} é seu ponto'.format(ponto) 

result = primeira_jogada()
print(result)

while True:
    if result == venceu or result == perdeu:
        break
    else:
        continuar = input("'ok' para continuar:  ")
        if continuar == 'ok':
            soma = jogada()
            if soma == 7:
                print('perdeu')
                break
            elif soma == ponto:
                print('yay, ganhou')
                break
            
                
    
    
    
    

    
