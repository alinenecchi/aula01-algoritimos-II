class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print('Código: {} Nome: {} Matrícula: {}'
              .format(str(self.codigo).ljust(5),
                      self.nome.ljust(11),
                      self.matricula).ljust(10))