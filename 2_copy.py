usuarios = open('usuarios.txt')
r = open('relatorio.txt', 'w')
mbs = []
ps = []
nomes = []
cabeçalho = """ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso\n\n"""
r.write(cabeçalho)

def b_mb(b):
    b = int(b)
    mb = b/10**6
    mbs.append(mb)
    return

def relat(linha):
    nomes.append(linha[:15])
    b_mb(linha[16:])   
    return

def total(lista):
    return sum(lista)

def porcentagem(lista):
    for e in lista:
        p = e*100/T
        ps.append(p)
    return ps

for l in usuarios.readlines():
    relat(l)
    
T = total(mbs)
porcentagem(mbs)

#fazer dict
y = 0
dic = {}
for n in nomes:
    dic[mbs[0+y]] = nomes[0+y]
    y = y + 1
dic = sorted(dic.items())

x = 0
while x < 6:
    r.write(f'{x+1}   {dic[0+x][1]}  {sorted(mbs)[0+x]: .2f} MB        {sorted(ps)[0+x]: .2f}%\n')
    x += 1
    
media = T/6
rodape = """\nEspaço total ocupado: {0: .2f} MB\nEspaço médio ocupado: {1: .2f} MB""".format(T, media)
r.write(rodape)

r.close()
usuarios.close()
