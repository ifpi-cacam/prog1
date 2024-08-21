"""
Programação Estruturada de Computadores
Aula dia 15/08/2024
Correção da Lista de Exercícios da Aula dia 14/08/2024
Questão4
"""
dias = []
dias.append('Segunda')
dias.append('Terça')
print(dias)
dias.append('Quarta')
dias.append('Sexta')
print(dias)
dias.insert(3, 'Quinta')
print(dias)
dias2 = ['Segunda', 'Terça']
dias.extend(dias2)
print(dias)
dias.insert(4, 'Quinta')
print(dias)
dias.reverse()
print(dias)
