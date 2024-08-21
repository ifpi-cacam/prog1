"""
Programação Estruturada de Computadores
Aula dia 15/08/2024
Correção da Lista de Exercícios da Aula dia 14/08/2024
Questão1
"""
# receber 4 variáveis, nome, idade, sexo, nota1 e nota2.

nome  = str(input('Digite o nome: '))
idade = int(input('Digite a idade: '))
sexo  = str(input('Digite o sexo: '))
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

# Declarar uma variável do tipo tupla aluno com 
# cada valor correspondente às variáveis
# recebidas
aluno = (nome, idade, sexo, nota1, nota2)

# Declarar uma variável média, que receberá a média 
# das notas na variável aluno
media = (aluno[3] + aluno[4])/2

# Mostrar todos os resultados dos dados da 
# variável aluno juntamente com a 
# média calculada.
print('Nome do aluno: ', aluno[0])
print('Idade do aluno: ', aluno[1])
print('Sexo do aluno: ', aluno[2])
print('Nota 1 do aluno: ', aluno[3])
print('Nota 2 do aluno: ', aluno[4])
print('Média do aluno: ', media)
