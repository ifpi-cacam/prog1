notas = [6, 7, 8, 9]
soma_notas = 0
indice = 0
while indice < len(notas):
    soma_notas += notas[indice]
    indice += 1
media = soma_notas / len(notas)
print("A média das notas é:", media)
