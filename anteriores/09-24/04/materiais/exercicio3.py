opcao = 'N'
precos = []
while(opcao=='N'):
    preco = float(input('Digite o preco do produto: '))
    precos.append(preco)
    opcao = str(input('Voce deseja finalizar?(S/N)'))

print('A soma dos precos é: ', sum(precos))
print('O maior preco é: ', max(precos))
print('O menor preco é: ', min(precos))
