import string

pessoas = list(string.ascii_uppercase[:5])
pesos = []
alturas = []

def peso_alt():
    for p in pessoas:
        peso = input('insira peso(kg):  ')
        pesos.append(peso)
        alt = input('insira altura(m):  ')
        alturas.append(alt)
    return pesos, alturas

peso_alt()
print(f'Pesos: {pesos[::-1]}\nAlturas: {alturas[::-1]}')
    
