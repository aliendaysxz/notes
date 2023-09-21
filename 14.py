from itertools import combinations, permutations


def validaTab(tabela): # Verifica se a tabela é válida
    if sum(tabela[:3]) == sum(tabela[3:6]) == sum(tabela[6:10]):
        if sum(tabela[::3]) == sum(tabela[1::3]) == sum(tabela[2::3]):
            if sum(tabela[::4]) == sum(tabela[2:8:2]):
                print(tabela, ' valida ')
                return 1
            else: return 0
        else: return 0
    else: return 0


def gera(tab): #gerar as matrizes possíveis
    cont = 0
    validos = 0
    for i in permutations(tab,9):
        cont += 1
        validos += validaTab(i)
    print(f'total de verificações {cont} e matriz válidas {validos}')

tabela = [1,2,3,4,5,6,7,8,9]

gera(tabela)
