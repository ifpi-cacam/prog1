"""
Estrutura de Repetição - While
Construa um script em Python para mostrar a soma de uma lista 
de numeros inteiros...
"""
numeros = [8, 3, 2, 4, 7, 5, 1, 6, 4]
x = 0
soma = 0
while(x<len(numeros)):
    soma = soma + numeros[x]
    x = x + 1
else:
    print('A soma é: ', soma)









