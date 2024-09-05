lista = [2, 4, 6, 7, 8, 10]
valor_procurado = 7
indice = 0
encontrado = False
while indice < len(lista):
    if lista[indice] == valor_procurado:
        encontrado = True
        break
    indice += 1
if encontrado:
    print("Valor encontrado na posição", indice)
else:
    print("Valor não encontrado na lista.")