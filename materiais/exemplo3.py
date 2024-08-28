"""
Estrutura de Repetição - While
Construa um script em Python para mostrar os valores de uma  
lista de nomes de cidades
"""
lista = ["Teresina", "Campo Maior", "Altos", "Piripiri", "LC"]
s = 0
while(s<len(lista)):
    print('Cidade '+ str(s) + ': '+ lista[s])
    s = s + 1
