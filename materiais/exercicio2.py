di = {'a': 1, 'b': -3, 'c': 4, 'd': -2, 'e': 8, 'f': 3}

print(di.values())
lista = list(di.values()) # lista = [1, -3, 4, 0]
print(lista)
indice = 0
soma = 0
while(indice<len(lista)):
    if(lista[indice]>0):
        soma = soma + lista[indice]
    indice = indice +1

print('A soma dos elementos positivos é: ',soma)