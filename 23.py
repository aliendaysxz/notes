import operator as op

us = open('usuarios.txt', 'r')
r = open('relatorio.txt', 'w')
dic = {}
mbs = []
nomes = []

def b_mb(b):
    b = int(b)
    mb = b/10**6
    mbs.append(mb)
    return mbs

for linha in us.readlines():
    nomes.append(linha[:15])
    b_mb(linha[15:])
total = sum(mbs)
media = total/6

a = 0
for n in nomes:
    dic[n] = mbs[0+a]
    a += 1

cab = """ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário      Espaço utilizado(MB)     % do uso\n"""
corpo = ''
rodape = """Espaço total ocupado: {:.2f} MB\n
Espaço médio ocupado: {:.2f} MB""".format(total, media)

r.write(cab)
print(cab)
b = 0
c = sorted(dic.items(), key=op.itemgetter(1), reverse=True)
for i in c:
    linha_tab = '{} {} {:.2f}                   {:.2f}\n'.format(b+1, i[0], i[1], float(i[1])*100/total)
    r.write(linha_tab)
    print(linha_tab)
    b += 1
r.write(rodape)
print(rodape)
r.close()
