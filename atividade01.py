'''Atividade Aula01 - Revisão Métodos e Listas
• Construir um algoritmo que contenha 3 listas:

      • Nomes de produtos

      • Preços de cada produto

      • Quantidades de cada produto

• Construir uma função para imprimir um dos produtos da lista 
e uma função para retirar um dos produtos das listas'''
menu = '''
Menu
0- Finalizar
1- Cadastrar Produto
2- Imprimir Produto
3- Retirar Produto
   Escolha: 

    '''

listaProdutos = ['CANETA', 'CADERNO']
listaPreco = [3.50, 12.00]
listaQuantidade = [3, 5]


def inserirProdutos():
    nome = str(input('Nome do produto: ')).upper()
    return listaProdutos.append(nome)


def inserirPreco():
    preco = float(input('Preço do produto: '))
    return listaPreco.append(preco)


def inserirQuantidade():
    qtde = int(input('Quantidade do produto: '))
    return listaQuantidade.append(qtde)


def relatorioProdutos():
    for ind, produto in enumerate(listaProdutos):
        print(produto)


def cadastrarProdutos():
    inserirProdutos()
    inserirPreco()
    inserirQuantidade()


def imprimirProdutos():
    print("----- Lista de produtos -----")
    print(" Produto                       preço            quantidade")

    for ind, produto in enumerate(listaProdutos):
        print(" {0} {1} {2}"
            .format(
            str(produto).ljust(25),
            str(listaPreco[ind]).center(13),
            str(listaQuantidade[ind]).center(23)
        )
        )


def retirarProduto():
    relatorioProdutos()
    produto = str(input('Digite o nome do produto que deseja retirar: ')).upper()
    if produto in listaProdutos:
        ind = listaProdutos.index(produto)
        listaProdutos.pop(ind)
        listaPreco.pop(ind)
        listaQuantidade.pop(ind)
        input('Produto removido da lista. [Enter]')
    else:
        input('Produto não consta na lista. [Enter]')

    # input('[Enter] Continua...')


# Programa Principal 
escolha = 0
while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
        cadastrarProdutos()
    elif escolha == '2':
        imprimirProdutos()
    elif escolha == '3':
        retirarProduto()
    else:
        input('Opção inválida! [Enter]')