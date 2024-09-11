meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril',
         'Maio','Junho','Julho','Agosto',
         'Setembro','Outubro','Novembro','Dezembro']
temp = {}
i = 0
while(i<12):
    t = float(input('Digite a temperatura no mes: '+meses[i]+': '))
    temp[i] = t
    i = i + 1

# Letra a)  Mostrar todas as temperaturas
for x in temp:
    print(temp[x])

# Letra b)  Mostrar a média das temperaturas
# Somar todas as médias
soma = 0
for x in temp:
    soma = soma + temp[x]
print('A média das temperaturas é: ', soma/len(temp))

# Letra c)
i = 0
print('Temperaturas do 1o Semestre: ')
while(i<6):
    print('Mes: ', meses[i], ':', temp[i])
    i = i + 1

i = 6
print('Temperaturas do 2o Semestre: ')
while(i<12):
    print('Mes: ', meses[i], ':', temp[i])
    i = i+1
