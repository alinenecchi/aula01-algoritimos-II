from pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, nome, endereco, telefone, cnpj, inscricaoEstadual, quantidadeFuncionarios):
        Pessoa.__init__(self, nome, endereco, telefone)
        self._cnpj = cnpj
        self._inscricaoEstadual = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios