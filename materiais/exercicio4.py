lista = [1, 4, 5, 8, 2, 7, 4, 7, 7, 3, 3, 7, 1, 5, 2, 4]
indice = 0
while(indice<len(lista)):
    print(lista[indice])
    print('O elemento ', lista[indice], 'se repete ', lista.count(lista[indice]))
    indice = indice + 1

l2 = ['Maca', 'Banana', 'Uva', 'Maca', 'Maca']
print('Maca se repete: ', l2.count('Maca'), 'vezes')