lista = [4, 7, -2, 9, -5, 3]
soma = 0
indice = 0
while indice < len(lista):
    if lista[indice] > 0:
        soma += lista[indice]
    indice += 1
print("A soma dos números positivos é:", soma)