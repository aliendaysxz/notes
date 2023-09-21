import random
import string

alunos = list(string.ascii_uppercase[:10])
dic = {}
medias7 = {}
    
def sext_dic():
    medias = []
    for a in alunos:
        notas = random.sample(list(range(0,11)), 4)
        m = sum(notas)/4
        m = str(m)
        medias.append(m)
        
    a = 0
    for m in medias:
        dic[alunos[0+a]] = m
        a = a + 1
        
    return dic

def sext_medias7():
    dic = sext_dic()
    for d in dic.items():
        if float(d[1]) >= 7:
            medias7.update({d[0] : d[1]})
        else:
            continue
    return medias7

        
sext_medias7()
print('MÉDIAS MAIORES OU IGUAIS A 7\n')
for e in medias7.items():
    print('aluno {}, média {}'.format(e[0],e[1]))



        


    


