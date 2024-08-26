plantas = {}

# Letra a)
qp = int(input('Digite a quantidade de plantas (min. 8): '))
for p in range(qp):
    nome = str(input('Nome da planta: '))
    qml = int(input('Quantidade de ml: '))
    plantas[nome] = qml

# Letra b)
total = 0
for p in plantas:
    total = total + plantas[p]
print('Total de agua para todas as plantas (ml): ', total)

# Letra c)
for p in plantas:
    print('Nome da planta: ', p)
    print('Quantidade em ml: ', plantas[p])

# Letra d)
lista = []
for p in plantas:
    lista.append(plantas[p])

print('Maior valor gasto em ml', max(lista))
print('Menor valor gasto em ml', min(lista))















