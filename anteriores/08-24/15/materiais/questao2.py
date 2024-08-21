"""
Programação Estruturada de Computadores
Aula dia 15/08/2024
Correção da Lista de Exercícios da Aula dia 14/08/2024
Questão2
"""

# a) Declare 2 variáveis do tipo tupla, empregado1 e empregado2 
# com os valores, para cada um: nome, idade e salário. Receba 
# tais valores por meio da entrada padrão do Python input
empregado1 = (
    str(input('Digite o nome do empregado 1: ')), 
    int(input('Digite a idade do empregado 1: ')),
    float(input('Digite o salário do empregado 1: ')) 
    )

empregado2 = (
    str(input('Digite o nome do empregado 2: ')), 
    int(input('Digite a idade do empregado 2: ')),
    float(input('Digite o salário do empregado 2: ')) 
    )

print(empregado1)
print(empregado2)

# b) Calcule e mostre a diferença entre os salários
difSal = empregado1[2] - empregado2[2]
print('Diferença entre os salários dos empregados; ', difSal)

# c) Calcule e mostre a diferença entre as idades
difIda = empregado1[1] - empregado2[1]
print('Diferença entre as idades dos empregados; ', difIda)



