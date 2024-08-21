"""
Construa um script em Python para receber as 10 notas 
de um aluno, salvá-las em uma lista e:
a) Mostrar a maior nota
b) Mostrar a menor nota
c) Mostrar a média
"""
notas = []
soma = 0
for n in range(10):
    nota = float(input('Nota ' + str(n+1) + ': '))
    notas.append(nota)
    soma = soma + nota

print(notas)
print('A maior nota é: ', max(notas))
print('A menor nota é: ', min(notas))
print('A média nota é: ', soma/len(notas))
print('A média nota é: ', sum(notas)/len(notas))