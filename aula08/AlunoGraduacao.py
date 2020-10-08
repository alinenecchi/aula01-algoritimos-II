from Aluno import Aluno

class AlunoGraduacao(Aluno):

    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        print('Código: {}  Nome: {}  Matrícula: {} Semestre: {}'
              .format(str(self.codigo).ljust(4),
                      self.nome.ljust(10),
                      self.matricula.ljust(12),
                      str(self.semestre)))