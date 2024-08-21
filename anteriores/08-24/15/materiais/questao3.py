"""
Programação Estruturada de Computadores
Aula dia 15/08/2024
Correção da Lista de Exercícios da Aula dia 14/08/2024
Questão3
"""
aluno1 = []
aluno2 = []

# Atribuindo os dados para a lista do primeiro aluno (aluno1)
aluno1.insert(0, 'Maria')
aluno1.insert(1, 22)
aluno1.insert(2, 7.5)
aluno1.insert(3, 2.5)
aluno1.insert(4, 5.0)
print(aluno1)
print('Aluno1/Nome: ', aluno1[0])
print('Aluno1/Idade: ', aluno1[1])
print('Aluno1/Nota 1: ', aluno1[2])
print('Aluno1/Nota 2', aluno1[3])
print('Aluno1/Nota 3', aluno1[4])

# Atribuindo os dados para a lista do segundo aluno (aluno2)
aluno2.insert(0, 'Jose')
aluno2.insert(1, 16)
aluno2.insert(2, 3.5)
aluno2.insert(3, 8.5)
aluno2.insert(4, 7.2)
print(aluno2)
print('Aluno2/Nome: ', aluno2[0])
print('Aluno2/Idade: ', aluno2[1])
print('Aluno2/Nota 1: ', aluno2[2])
print('Aluno2/Nota 2', aluno2[3])
print('Aluno2/Nota 3', aluno2[4])

soma1 = aluno1[2] +aluno1[3] +aluno1[4]
media1 = soma1/3
print('Aluno1/Média: ', media1)

soma2 = aluno2[2] +aluno2[3] +aluno2[4]
media2 = soma2/3
print('Aluno2/Média: ', media2)

# Comparando as idades - Letra f)
if(aluno1[1]>aluno2[1]):
    print('O Aluno ', aluno1[0], 'possui maior idade')
else:
    if(aluno2[1]>aluno1[1]):
        print('O Aluno ', aluno2[0], 'possui maior idade')
    else:
        print('As idades dos alunos sao iguais!')
# Comparando as médias - Letra g)
if(media1>media2):
    print('O Aluno ', aluno1[0], 'possui maior média')
else:
    if(media2>media1):
        print('O Aluno ', aluno2[0], 'possui maior média')
    else:
        print('As médias dos alunos sao iguais!')






