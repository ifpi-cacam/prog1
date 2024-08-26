n = int(input('Digite a quantidade de habitantes: '))

total_salario = 0
total_nfi = 0
num_1000 = 0
num_5 = 0

for x in range(n):
    sal = float(input('Qual seu salario? '))
    nfi = float(input('Quantos filhos voce tem? '))
    total_salario = total_salario +sal
    total_nfi = total_nfi + nfi
    if(sal<=1000):
        num_1000 = num_1000 + 1
    if(nfi>5):
        num_5 = num_5 + 1


media_sal = total_salario/n
media_nfi = total_nfi/n

print('A media do salario da populacao é: ', media_sal)
print('A media do numero de filhos da populacao é: ', media_nfi)
porc_1000 = (num_1000/n)*100
print('A porcentagem de pessoas que ganham ate 1000 reais é: ', porc_1000)
print('O total de pessoas que tem mais de 5 filhos e: ', num_5)









