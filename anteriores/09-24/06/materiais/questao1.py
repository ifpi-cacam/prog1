matriculas = [8734, 6444, 3744, 1192, 2234]
nomes = ['Ana Oliveira', 'Marcelo Alves', 'Maria Júlia', 'Miguel Souza', 'Pedro Antônio']
idades = [29, 33, 18, 41, 22]
salarios = [2567.78, 4519.35, 3351.58, 8427.33, 2874.71]

# Matriculas com o For
print(matriculas)
for m in matriculas:
    print(m)

# Nomes com o For
print(nomes)
for n in nomes:
    print(n)

# Idades com o For
print(idades)
for i in idades:
    print(i)

# Salarios com o For
print(salarios)
for sl in salarios:
    print(sl)

# Letra a) Mostrar os dados das listas
i = 0
while(i<len(matriculas)):
    print('Matricula: ', matriculas[i])
    print('Nome: ', nomes[i])
    print('Idade: ', idades[i])
    print('Salario: ', salarios[i])
    i = i+1

# Letra b) Mostrar a média das idades
media_idades = sum(idades)/len(idades)
print('A media das idades é: ', media_idades)

# Letra c) Media dos salarios, maior e menor salario
media_sal = sum(salarios)/len(salarios)
maior_sal = max(salarios)
menor_sal = min(salarios)
print('A media dos salarios é: ', media_sal)
print('O maior salário é: ', maior_sal)
print('O menor salário é: ', menor_sal)

# Letra d) 
diferenca = maior_sal - menor_sal
print('Diferenca entre o maior e o menor salário: ', diferenca)
