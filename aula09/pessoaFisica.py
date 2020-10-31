from pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = float(peso)
        self.altura = float(altura)
        self.imc = 0

    def imprimir__cpf(self):
        print(self.cpf)

    def calculo_imc(self):
        self.imc = self.peso / (self.altura*self.peso)
        return self.imc
    
    def imprimir_imc(self):
        print(f"O IMC de %p é %i" % (self.nome, self.calculo_imc()))
        
    def imprimir_altura(self):
        print(self.altura)
        
    def imprimir_peso(self):
        print(self.peso)
        
    
    