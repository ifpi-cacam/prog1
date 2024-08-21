"""
Comandos em Python - comando range()
Serve para mostrar uma faixa de valores inteiros
range(n) - Mostra todos os valores inteiros entre 0 e n
Comando range() é usado juntamente com o comando for  
em estruturas de repetição para iterar entre valores
"""
# Exemplo1 - mostrando uma faixa de valores range(5) - 0, 1, 2, 3, 4
print(range(5))

# Mostrando tais valores como listas - convertendo de range para list
print(list(range(5)))

# Percorrendo os valores de um range com estrutura de repetição for
for x in range(5):
    print(x)

# Usando o Range para mostrar os valores de uma lista de 5 elementos
lista_frutas = ['Pera', 'Uva', 'Goiaba', 'Melancia', 'Kiwi']
# Primeira forma - SEM o uso de range
for x in lista_frutas:
    print(x)

# Segunda forma - COM o uso de range
for x in range(len(lista_frutas)): # Len = retorna a quantidade de elementos da lista - no caso, 5
    print(lista_frutas[x]) # x nesse caso se refere a um índice inteiro da posição de cada elemento na lista de frutas
