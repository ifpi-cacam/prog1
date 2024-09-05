lista_original = [12, 23, 34, 45, 56]
lista_pares = []
indice = 0
while indice < len(lista_original):
    if lista_original[indice] % 2 == 0:
        lista_pares.append(lista_original[indice])
    indice += 1
print("Lista de números pares:", lista_pares)