opcao = 10
lista_opcoes = 6*[0]
num_votos = 0
while opcao != 0:    
    opcao = int(input("Digite a opção de sistema opercional utilizado na sua organização:\n1 - Windows Server\n2 - Unix\n3 - Linux\n4 - Netware\n5 - Mac OS\n6 - Outro\nOpção escolhida:  "))
    
    if opcao > 6 or opcao < 0:
        print('Número inválido, tente outra opção!')
    elif opcao == 0:
        print('\nPesquisa finalizada!')
        break
    else:
        lista_opcoes[opcao-1] += 1 
        num_votos = num_votos + 1   

opcoes = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']


melhor = 0
print('Sistema Operacional     Votos  %')
print('----------------------------------')
for idx in range(len(lista_opcoes)):
    porcent = (lista_opcoes[idx]/num_votos)*100
    print(f'{opcoes[idx]}   -  {str(lista_opcoes[idx])}  -  {porcent:.2f}')
    if lista_opcoes[idx] > lista_opcoes[melhor]:
        melhor = idx


print(f'\nTotal de votos: {num_votos}')
porcentagem_melhor = (lista_opcoes[melhor]/num_votos)*100
print(f'O Sistema Operacional mais votado foi o {opcoes[melhor]}, com {lista_opcoes[melhor]} votos, correspondendo a {porcentagem_melhor:.2f} dos votos.')
