import json

livros = []

def salvar():
    # Salvar os dados
    with open("livros.txt", "w") as fp:
        json.dump(livros, fp)

def recuperar():
    # Recuperar os Dados
    with open("livros.txt", "r") as fp:
        livros = json.load(fp)

salvar()
recuperar()

def menuInicial():
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

def cadastrarLivro():
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
    salvar()
    recuperar()
    print('LIVRO CADASTRADO COM SUCESSO!')
    input()

def pesquisarPorMatricula():
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

def editarPorMatricula():
    print("------------ SISTEMA DE CADASTRO DE LIVROS -----------------")
    print("---- 3) EDITAR LIVRO POR MATRÍCULA -------------------------")
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
        mat = int(input('Digite a NOVA matricula: '))
        tit = str(input('Digite o NOVO titulo: '))
        aut = str(input('Digite o NOVO autor: '))
        edi = str(input('Digite a NOVA editora: '))
        ano = int(input('Digite o NOVO ano: '))
        pre = float(input('Digite o NOVO preco: '))
        livro = {}
        livro['Matricula'] = mat
        livro['Titulo'] = tit
        livro['Autor'] = aut
        livro['Editora'] = edi
        livro['Ano'] = ano
        livro['Preco'] = pre
        livros[encontrado] = livro
        print('LIVRO CADASTRADO COM SUCESSO!')
    input()

def excluirPorMatricula():
    print("------------ SISTEMA DE CADASTRO DE LIVROS -----------------")
    print("---- 4) EXCLUIR LIVRO POR MATRÍCULA ------------------------")
    input()

def pesquisarPorAno():
    print("------------ SISTEMA DE CADASTRO DE LIVROS -----------------")
    print("---- 5) PESQUISAR LIVRO POR ANO ----------------------------")
    input()

def pesquisarPorAutor():
    print("------------ SISTEMA DE CADASTRO DE LIVROS -----------------")
    print("---- 6) PESQUISAR LIVRO POR AUTOR --------------------------")
    input()


def mostrarTodosLivros():
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


opcao = 10
while(opcao!=0):
    menuInicial()    
    opcao = int(input('Selecione uma opcao> '))
    
    if(opcao==1):
        cadastrarLivro()
    
    if(opcao==2):
        pesquisarPorMatricula()
    
    if(opcao==3):
        editarPorMatricula()

    if(opcao==4):
        excluirPorMatricula()

    if(opcao==5):
        pesquisarPorAno()

    if(opcao==6):
        pesquisarPorAutor()

    if(opcao==7):
        mostrarTodosLivros()
else:
    print('Voce saiu do sistema!')

















