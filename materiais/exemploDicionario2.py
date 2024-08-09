# Criando a variável lista (3 elementos)
alunos = {"Sérgio":8.5, "Márcia":4.5, "Mauro":6.5 }

# Mostrando a variável
print(alunos)

# Acessando os elementos
print(alunos["Sérgio"])
print(alunos["Márcia"])
print(alunos["Mauro"])

# Adicionando um valor
# Sempre ao final
alunos["Pedro"] = 2.5
print(alunos)

# Alterando um valor
alunos["Sérgio"] = 1.5
print(alunos)

# Removendo um valor/chave
del alunos["Mauro"]
print(alunos)


