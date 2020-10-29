from veiculo import Veiculo
class bicicleta(veiculo):
    def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro):
        veiculo.__init__(self, marca, qtdRodas, modelo)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimirInformacoesBicicleta(self):
        print(' BICICLETA - Marca: {}  - Qnt. Rodas: {}'
            '- Modelo: {} - Numero de marchas: {} - Bagageiro: {}'
                .format(self.marca, self.qtdRodas, self.modelo, self.numMarchas, self.bagageiro))