class veiculo:
    def __init__(self, marca, qtdRodas, modelo):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, valor):
        if valor > 0:
            self.velocidade += valor

    def frear(self, valor):
        if valor > 0:
            self.velocidade -= valor
            if self.velocidade < 0:
                self.velocidade = 0

    def imprimirInformacoesVeiculo(self):
        print(self.__dict__)