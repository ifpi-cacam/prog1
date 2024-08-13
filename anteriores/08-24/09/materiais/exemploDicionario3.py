# Criando a variável lista (3 elementos)
alunos = {}

al1 = str(input('Nome 1o Aluno: '))
alunos[al1] = float(input('Nota 1o Aluno: ')) 

al2 = str(input('Nome 2o Aluno: '))
alunos[al2] = float(input('Nota 2o Aluno: ')) 

al3 = str(input('Nome 3o Aluno: '))
alunos[al3] = float(input('Nota 3o Aluno: '))

print('Nomes (Chaves)', alunos.keys())
print('Notas (Valores)', alunos.values())

