"""
Construa um Script em Python para declarar as 5 médias 
de um aluno, da seguinte forma:

medias = [1.5, 10.0, 5.5, 4.2, 2.1]

O script deve percorrer a lista de médias e, para cada 
média, mostrar seu valor e mostrar a situação do aluno:

APROVADO -> media >=7.0
EXAME FINAL 7.0> media >= 4.0
REPROVADO -> 4.0 >media

"""
medias = [1.5, 10.0, 5.5, 4.2, 2.1]
for m in medias:
    print("Média: ", m)
    if (m>=7.0):
        print('APROVADO!')
    if( 7.0>m>=4.0):
        print('EXAME FINAL!')
    if( 4.0>m):
        print('REPROVADO!')

