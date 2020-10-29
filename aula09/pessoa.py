class Pessoa:
    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.telefone = telefone

    def imprimir_nome(self):
        print(self.nome)

    def imprimir_telefone(self):
        print(self.telefone)

    def imprimir(self):
        print('Código: {} Nome: {} Endereço: {} Telefone: {}'
              .format(str(self.__codigo).ljust(5),
                      self.nome.ljust(11),
                      self._endereco.ljust(12),
                      str(self.telefone)))