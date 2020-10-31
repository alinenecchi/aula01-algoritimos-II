from pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, nome, endereco, telefone, cnpj, inscricaoEstadual, quantidadeFuncionarios):
        Pessoa.__init__(self, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios
        
    def Imprimir_cnpj(self):
        print(self.__cnpj)
        
    def Imprimir_IE(self):
        print(self.__inscricaoEstadual)
        
    def Imprimir_Qtde_funcionarios(self):
        print(self.quantidadeFuncionarios)