livros = []
opcao = 10
while(opcao!=0):
    print("------------ SISTEMA DE CADASTRO DE LIVROS -----------------")
    print("---- MENU INICIAL ------------------------------------------")
    print("---- 1) CADASTRAR NOVO LIVRO -------------------------------")
    print("---- 2) PESQUISAR LIVRO POR MATRÍCULA ----------------------")
    print("---- 3) EDITAR LIVRO POR MATRÍCULA -------------------------")
    print("---- 4) EXCLUIR LIVRO POR MATRÍCULA ------------------------")
    print("---- 5) PESQUISAR LIVRO POR ANO ----------------------------")
    print("---- 6) PESQUISAR LIVRO POR AUTOR --------------------------")
    print("---- 7) MOSTRAR TODOS OS LIVROS ----------------------------")
    print("---- 0) SAIR -----------------------------------------------")
    opcao = int(input('Selecione uma opcao> '))
    if(opcao==1):
        print("------------ SISTEMA DE CADASTRO DE LIVROS -----------------")
        print("---- 1) CADASTRAR NOVO LIVRO -------------------------------")
        mat = int(input('Digite a matricula: '))
        tit = str(input('Digite o titulo: '))
        aut = str(input('Digite o autor: '))
        edi = str(input('Digite a editora: '))
        ano = int(input('Digite o ano: '))
        pre = float(input('Digite o preco: '))
        livro = {}
        livro['Matricula'] = mat
        livro['Titulo'] = tit
        livro['Autor'] = aut
        livro['Editora'] = edi
        livro['Ano'] = ano
        livro['Preco'] = pre
        livros.append(livro)
        print('LIVRO CADASTRADO COM SUCESSO!')
        input()

    if(opcao==2):
        print("------------ SISTEMA DE CADASTRO DE LIVROS -----------------")
        print("---- 2) PESQUISAR LIVRO POR MATRÍCULA ----------------------")
        matricula = int(input('Digite a matricula a ser pesquisada: '))
        indice = 0
        encontrado = -1
        while(indice<len(livros)):
            if(livros[indice]['Matricula']==matricula):
                encontrado = indice
                break
            indice = indice + 1
        if(encontrado==-1):
            print('Nenhum livro encontrado com essa matricula')
        else:
            print('Livro encontrado!!')
            print('Matricula do livro: ', livros[encontrado]['Matricula'])
            print('Titulo do livro: ', livros[encontrado]['Titulo'])
            print('Autor do livro: ', livros[encontrado]['Autor'])
            print('Editora do livro: ', livros[encontrado]['Editora'])
            print('Ano do livro: ', livros[encontrado]['Ano'])
            print('Preco do livro: ', livros[encontrado]['Preco'])
        input()

    if(opcao==3):
        print("------------ SISTEMA DE CADASTRO DE LIVROS -----------------")
        print("---- 3) EDITAR LIVRO POR MATRÍCULA -------------------------")
        input()

    if(opcao==4):
        print("------------ SISTEMA DE CADASTRO DE LIVROS -----------------")
        print("---- 4) EXCLUIR LIVRO POR MATRÍCULA ------------------------")
        input()

    if(opcao==5):
        print("------------ SISTEMA DE CADASTRO DE LIVROS -----------------")
        print("---- 5) PESQUISAR LIVRO POR ANO ----------------------------")
        input()

    if(opcao==6):
        print("------------ SISTEMA DE CADASTRO DE LIVROS -----------------")
        print("---- 6) PESQUISAR LIVRO POR AUTOR --------------------------")
        input()

    if(opcao==7):
        print("------------ SISTEMA DE CADASTRO DE LIVROS -----------------")
        print("---- 7) MOSTRAR TODOS OS LIVROS ----------------------------")
        for l in livros:
            print('Matricula do livro: ', l['Matricula'])
            print('Titulo do livro: ', l['Titulo'])
            print('Autor do livro: ', l['Autor'])
            print('Editora do livro: ', l['Editora'])
            print('Ano do livro: ', l['Ano'])
            print('Preco do livro: ', l['Preco'])
            print('------------------------------')
        input()
else:
    print('Voce saiu do sistema!')

















