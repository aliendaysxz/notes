def somaImposto(taxaImposto, custo):
    valor = custo + (custo*taxaImposto/100)
    print(valor)

custo = int(input('preço:  '))
taxaImposto = int(input('valor do importo(%):  '))

somaImposto(taxaImposto, custo)
