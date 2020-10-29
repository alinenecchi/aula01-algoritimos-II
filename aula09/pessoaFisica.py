from pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def imprimir__cpf(self):
        print(self.cpf)

    def calculo_imc(self):
        imc = self.peso / pow(self.altura)
        return imc
    
    