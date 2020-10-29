from veiculo import Veiculo
class moto(automovel):
    def __init__(self, marca, qtdRodas, modelo, potMotor, partidaEletrica):
        automovel.__init__(self, marca, qtdRodas, modelo, potMotor)
        self.partidaEletrica = partidaEletrica

    def imprimirInformacoesMoto(self):
        print('MOTO - Marca: {} - Qnt. Rodas: {} - Modelo: {} '
              ' - Potencia do motor: {} - Partida Eletrica: {}'
            .format(self.marca, self.qtdRodas, self.modelo, self.potMotor, self.partidaEletrica))