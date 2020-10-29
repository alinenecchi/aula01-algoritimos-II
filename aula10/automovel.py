from veiculo import Veiculo
class automovel(veiculo):
    def __init__(self, marca, qtdRodas, modelo, potMotor):
        veiculo.__init__(self, marca, qtdRodas, modelo)
        self.potMotor = potMotor

    def imprimirInformacoesAutomovel(self):
        print('Automovel: ')
        print(self.__dict__)