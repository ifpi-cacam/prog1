"""
Programação Estruturada de Computadores
Aula dia 15/08/2024
Correção da Lista de Exercícios da Aula dia 14/08/2024
Questão5
"""
frutas = {}
frutas['Maca'] = 12.55
frutas['Banana'] = 7.75
frutas['Uva'] = 22.50
frutas['Laranja'] = 4.75
frutas['Ameixa'] = 23.55

print(frutas)

frutas['Melao'] = '10.25'

nome = str(input('Digite o nome da fruta:'))
q = int(input('Digite a quantidade:'))
total = frutas[nome] * q
print('O total gasto com ', nome, 'e quantidade ', q, 'é: ', total)

totalc = frutas['Maca'] + frutas['Banana'] + frutas['Uva'] + frutas['Laranja'] + frutas['Ameixa']  
print('Total gasto com 1kg de cada fruta: ', totalc)

frutas['Uva'] = 18.55
frutas['Laranja'] = 2.10




