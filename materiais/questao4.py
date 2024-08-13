numeros = []

numeros.append(int(input('Digite o primeiro numero: ')))
numeros.append(int(input('Digite o segundo numero: ')))
numeros.append(int(input('Digite o terceiro numero: ')))
numeros.append(int(input('Digite o quarto numero: ')))
numeros.append(int(input('Digite o quinto numero: ')))
print(numeros)

numeros.append(10)
print(numeros)

del numeros[1]
print(numeros)

numeros[2] = 99
print(numeros)

soma = sum(numeros)
print('Soma dos valores: ', soma)

media = soma/len(numeros)

print('Média dos elementos da lista: ', media)

