idades = [18, 23, 15, 44, 11, 57, 62]

# a) Mostrar as idades
print('Mostrar toda a lista das idades')
for i in idades:
    print(i)

# b) 
print('Mostrar somente as idades maiores que 18')
indice = 0
while(indice<len(idades)):
    if(idades[indice]>18):
        print(idades[indice])
    indice = indice + 1

# c)
print('Mostrar somente as idades menores que 16')
indice = 0
while(indice<len(idades)):
    if(idades[indice]<16):
        print(idades[indice])
    indice = indice + 1

# d)
print('A maior idade é: ', max(idades))
print('A menor idade é: ', min(idades))
