# Primeira forma - sem usar listas
soma = 0
for x in range(101):
    if(x%2==0):
        soma = soma + x
print('Soma dos pares entre 0 e 100: ', soma)

# Segunda forma - sem usar if
soma = 0
for x in range(0, 101, 2):
    soma = soma + x
print('Soma dos pares entre 0 e 100: ', soma)

# Terceira forma - usando listas
pares = []
for x in range(101):
    if(x%2==0):
        pares.append(x)
print('Soma dos pares entre 0 e 100: ', sum(pares))

pares = []
# Quarta forma - preenchendo uma lista
pares = [x for x in range(0, 101, 2)]
print('Soma dos pares entre 0 e 100: ', sum(pares))
