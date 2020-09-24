menu = '''
Menu
0- Finalizar
1- Cadastro 
2- Imprimir
   Escolha: 
    '''

dicionario = {}


def cadastro():
    while True:
        try:
            nome = str(input("Digite o nome do aluno: "))
            if len(nome) == 0:
                input("Digite um nome válido.")
            else:
                nota1 = float(input("Digite a primeira nota: "))
                nota2 = float(input("Digite a primeira nota: "))
                media = (nota1 + nota2) / 2
                dicionario[nome] = str(media)
                return ()
        except:
            input("Erro ocorreu.")
            break


def imprimir():
    print("Nome       -         Média")
    for chave, valor in dicionario.items():
        print(f"{chave.ljust(20)}  {valor.ljust(20)}")


escolha = 0
while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
        cadastro()
    elif escolha == '2':
        imprimir()
    else:
        input('Opção inválida! [Enter]')