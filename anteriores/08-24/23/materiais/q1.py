modelo1 = str(input('Modelo do Veiculo 1: '))
marca1  = str(input('Marca do Veiculo 1: '))
cor1    = str(input('Cor do Veiculo 1: '))
ano1    = int(input('Ano do Veiculo 1: '))
quilom1 = int(input('Quilometragem do Veiculo 1: '))
preco1  = float(input('Preço do Veiculo 1: '))

veiculo1 = (modelo1, marca1, cor1, ano1, quilom1, preco1)

modelo2 = str(input('Modelo do Veiculo 2: '))
marca2  = str(input('Marca do Veiculo 2: '))
cor2    = str(input('Cor do Veiculo 2: '))
ano2    = int(input('Ano do Veiculo 2: '))
quilom2 = int(input('Quilometragem do Veiculo 2: '))
preco2  = float(input('Preço do Veiculo 2: '))

veiculo2 = (modelo2, marca2, cor2, ano2, quilom2, preco2)

print(veiculo1)
print(veiculo2)

if(veiculo1[4]>veiculo2[4]):
    print('Veiculo 1 possui maior quilometragem!')
else:
    if(veiculo2[4]>veiculo1[4]):
        print('Veiculo 2 possui maior quilometragem!')
    else:
        print('As quilometragens são iguais!')

if(veiculo1[5]>veiculo2[5]):
    print('Veiculo 1 possui maior preco!')
else:
    if(veiculo2[5]>veiculo1[5]):
        print('Veiculo 2 possui maior preco!')
    else:
        print('Os precos são iguais!')

