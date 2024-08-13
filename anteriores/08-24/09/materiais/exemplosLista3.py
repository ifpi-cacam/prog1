notas = [7.5, 2.5, 5.5]
print(notas)
notas[0] = notas[0] + notas[1]
print(notas)
notas[len(notas)-1] = 9.8
print(notas)
notas.append(2.5)
print(notas)
notas2 = [8.0, 1.1]
notas.extend(notas2)
print(notas)
print('Quant. 2.5?', notas.count(2.5))
print('Pos. 9.8: ', notas.index(9.8))
notas.insert(5, 0.5)
print(notas)
notas.pop(0)
print(notas)
del notas[0]
print(notas)
notas.remove(8.0)
print(notas)
notas.reverse()
print(notas)
notas.sort()
print(notas)
print('Soma: ', sum(notas))


# Exemplo de Tupla com tipos diferentes
aluno    = ('Maria Silva', 7.5, 18, 'APROVADO')
produto1 = ('Arroz', 2.55, 'Alimentos', 'OK', False)
produto2 = ('Sabonete', 1.55, 'Higiene', 'OK', True)

# Exemplo de Lista com tipos diferentes
funcionario = ['Pedro José', 'MASC', True, 'Teresina', 2590.55]
disc = ['Matematica', 'Exatas', False, 250, 255.65]


