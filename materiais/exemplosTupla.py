
# Criando a variável tupla (4 elementos)
disc =('MATE', 'HIST', 'FISI', 'QUIM')

# Mostrando o tipo da variável
print(type(disc))

# Acessando o primeiro elemento
print(disc[0])

# Acessando o último elemento da tupla
# O índice também pode ser uma variável
ultimo = 3
print(disc[ultimo])

# Mostrando o tamanho da tupla
print(len(disc))

print(type(disc.count))

# Não tentar alterar um elemento (erro!)
#disc[0] = "BIOL"

# Não acessar um elemento com índice inexistente
print('Posição 5:', disc[3])


nomes = ('Jose', 'Maria', 'Maria')
print('Indice: ', nomes.count('Maria'))

items = ('Maria', 2.5, 40, False)
print('Item 3: ', items[3])
