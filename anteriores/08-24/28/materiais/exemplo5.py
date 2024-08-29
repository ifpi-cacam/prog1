"""
Estrutura de Repetição - While
Construa um script em Python para declara um dicionario para 
armazenar uma lista de produtos com seus respectivos precos.
O script deve solicar nome e valor do produto ate que o usuario 
peça para finalizar. Ao final, deve mostrar os produtos...
"""
produtos = {}
opcao = 'S'
while(opcao=='S'):
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preco do produto: '))
    produtos[nome] = preco
    opcao = str(input('Deseja continuar?(S/N)'))
else:
    print('Você finalizou o cadastro!')

print(produtos)
