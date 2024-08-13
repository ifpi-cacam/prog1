
# Criando a variável lista (3 elementos)
livros =["Algoritmos", "Redes", "Web Design"]
print(livros)

# Acessando um elemento qualquer da lista
# O índice também pode ser uma variável
indice = 2
print(livros[indice])

# Alterando os elementos 1 e 3
livros[0] = "Prog. Mobile"
livros[2] = "Lógica de Prog."
print(livros)

# Removendo elemento
livros.remove("Redes")
print(livros)

# Adicionando elemento ao final
livros.append("Redes II")
print(livros)

# Somando uma segunda lista
livrosweb = ["Back-End", "Front-End"]
livros = livros + livrosweb
print(livros)

livros.extend(["Compiladores"])
print(livros)

del livros[0]

print(livros)

