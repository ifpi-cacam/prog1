lista    =  [1, 2, 3, 4, 5, 6, 8, 10, 11, 0, 6]
indice = 0
listainv = []

while(indice<len(lista)):
    listainv.insert(0, lista[indice])
    indice = indice + 1

print('Lista original: ', lista)
print('Lista invertida: ', listainv)
