from Fila import Fila 

fila = Fila()
def menu():
    resposta = input(''' 
+-----------------------------------------+
|             Menu Principal              |
+-----------------------------------------+
| 0 - Finalizar                           |
| 1 - Adicionar                           |
| 2 - Imprimir                            |
| 3 - Remover no inicio                   |
| 4 -                                     |
| 5 -                                     |
+-----------------------------------------+
Escolha:''')
    if resposta in ('0', '1', '2', '3', '4', '5'):
        return resposta
    input('Escolha incorreta. [Enter] - Tente Novamente.')
    return menu()


# Programa Principal
while True:
    escolha = menu()
    if escolha == '1':
        fila.adicionar(int(input("Digite um número: ")))
    elif escolha == '2':
        fila.imprimir()
    elif escolha == '3':
        fila.remover_inicio()
    elif escolha == '4':
        pass
    else:
        break
print('Fim')
