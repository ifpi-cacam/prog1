alturas = []

i = 0
while(i<4):
    altura = float(input('Digite a altura: '))
    alturas.append(altura)
    i = i+1

# Letra a)
print('Mostrando todas as alturas')
j = 0
while(j<len(alturas)):
    print(alturas[j])
    j = j +1

# Letra b)
print('Mostrando somente as alturas acima de 1.70')
p = 0
while(p<len(alturas)):
    if(alturas[p]>1.70):
        print(alturas[p])
    p = p +1

# Letra c) 
soma = 0
p = 0
while(p<len(alturas)):
    soma = soma + alturas[p]
    p = p +1

print('A média das alturas é: ', soma/len(alturas))


