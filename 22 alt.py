print('Defeitos:\n1 - Necessita de Esfera\n2 - Necessita de limpeza\n3 - Necessita troca de cabo ou conector\n4 - Quebrado ou inutilizado')
defeitos_ = ['Necessita de Esfera','Necessita de limpeza','Necessita troca de cabo ou conector','Quebrado ou inutilizado']


num_mouses = int(input('Quantos mouses defeituosos existem: '))
defeitos = 4*[0]

print('')
for idx in range(num_mouses):
    
    validacao = True
    while validacao:
        defeito = int(input('Qual o código do problema do mouse '+str(idx+1)+': '))
        if (defeito == 1) or (defeito == 2) or (defeito == 3) or (defeito == 4):
            validacao = False
        else:
            print('Número inválido, tente outro!')
    defeitos[defeito-1] = defeitos[defeito-1] + 1

for idx in range(len(defeitos_)):
    print(defeitos_[idx]+' - ' +str(defeitos[idx])+ ' defeitos - ' +str(defeitos[idx]*100/num_mouses)+'%' )
