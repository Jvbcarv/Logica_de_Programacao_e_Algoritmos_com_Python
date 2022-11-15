listaProdutos = []

#---------Começo da Função cadastrarProduto-------------------
def cadastrarProduto (cod):
    print('Bem-vindo(a) ao CADASTRAR Produtos')
    print('O código do produto a ser cadastrado é: {}' .format(cod))
    nome = input('Insira o nome do produto: ')
    fabricante = input('Insira o fabricante do produto: ')
    valor = float(input('Insira o valor do produto: '))
    dicionarioProduto = {'cod': cod, 'nome': nome, 'fabricante': fabricante, 'valor': valor}
    listaProdutos.append(dicionarioProduto.copy())
#---------Fim da Função cadastrarProduto--------------------

#---------Começo da Função consultarProduto-----------------
def consultarProduto ( ):
    while True:
        try:
            print('Bem-vindo(a) ao CONSULTAR Produtos')
            opConsultar = int(input('Entre com a opção desejada: \n1 - Consultar Todos produtos \n2- Consultar por código \n3- Consultar por fabricante \n4-Retornar \n>>'))
            if opConsultar == 1:
                print('bem-vindo a consultar TODOS os produtos')
                for produtos in listaProdutos:
                    for key, value in produtos.items():
                        print("{} : {}" .format(key, value))
            elif opConsultar == 2:
                print('bem-vindo a consultar CÓDIGO')
                entrada = int(input('Digite o código desejado: '))
                for produtos in listaProdutos:
                    if(produtos['cod'] == entrada):
                        for key, value in produtos.items():
                            print("{} : {}".format(key, value))
            elif opConsultar == 3:
                print('bem-vindo a consultar FABRICANTE')
                entrada = input('Digite o fabricante desejado: ')
                for produtos in listaProdutos:
                    if (produtos['fabricante'] == entrada):
                        for key, value in produtos.items():
                            print("{} : {}".format(key, value))
            elif opConsultar == 4:
                break
            else:
                print('O número digitado não está no menú. Tente de novo.')
                continue
        except ValueError:
            print('Pare de digitar números não inteiros.')
# ---------Fim da Função consultarProduto-------------------

# ----------Começo da Função removerProduto-----------------
def removerProduto():
    print('Bem-vindo(a) ao REMOVER Produtos')
    entrada = int(input('Digite o código desejado: '))
    for produtos in listaProdutos:
        if (produtos['cod'] == entrada):
            listaProdutos.remove(produtos)
# ----------Fim da Função removerProduto-----------------
# --------------------Começo MAIN -------------------------
codigo = 0

print('Bem-vindo ao programa Controle de Produtos')
while True:
    try:
        opcao = int(input('Digite a opção desejada: \n1 - Cadastrar Produto \n2 - Consultar Produto(s) \n3 - Remover Produto \n4 - Sair \n>>'))
        if opcao == 1:
            codigo = codigo + 1
            cadastrarProduto(codigo)
        elif opcao == 2:
            consultarProduto()
        elif opcao == 3:
            removerProduto()
        elif opcao == 4:
            break
        else:
            print('O número digitado não está no menú. Tente de novo.')
            continue
    except ValueError:
        print('Pare de digitar números não inteiros.')
# --------------------Fim do MAIN--------------------------

