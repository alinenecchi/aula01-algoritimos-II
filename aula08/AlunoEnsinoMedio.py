from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):

    def __init__(self,codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        print('Código: {} Nome: {} Matrícula: {} Ano: {}'
              .format(str(self.codigo).ljust(5),
                      self.nome.ljust(11), 
                      self.matricula.ljust(12),
                      str(self.ano)))