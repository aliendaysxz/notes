votos = [0]*23
num = 1000
num_votos = 0
while num != 0:    
    num = int(input("Digite o número do jogador (0=fim): "))
    if num > 23:
        print('Número inválido')
        continue
    else:
        votos[num-1] = votos[num-1] + 1 
        num_votos = num_votos + 1   
        
melhor = 0

print('\nForam computados '+str(num_votos)+ ' votos!\n')

print('Jogador  |   Votos   |    % de Votos   |')
print('========================================')
for idx in range(len(votos)):
    if votos[idx] > 0: 
    
        if idx >= 10:
            if votos[idx] < 10:
                print(f'  {idx+1}     |     {votos[idx]}     |       {(votos[idx]/num_votos)*100:.2f}     |')
            else:
                print(f'  {idx+1}     |     {votos[idx]}    |       {(votos[idx]/num_votos)*100:.2f}     |')
        else:
            if votos[idx] < 10:
                print(f'  {idx+1}      |     {votos[idx]}     |       {(votos[idx]/num_votos)*100:.2f}     |')
            else:
                print(f'  {idx+1}      |     {votos[idx]}    |       {(votos[idx]/num_votos)*100:.2f}     |')
            
    
    if votos[idx] > votos[melhor]:
         melhor = idx
print('========================================')


print(f'\nO melhor atleta foi o Camisa {idx+1}, com {votos[idx]} votos, correspondendo a {(votos[idx]/num_votos)*100:.2f} dos vtos válidos')
