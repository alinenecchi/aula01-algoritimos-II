from veiculo import Veiculo

class carro(automovel):
  def __init__(self, marca, qtdRodas, modelo, potMotor, qtdPortas):
    automovel.__init__(self, marca, qtdRodas, modelo, potMotor)
    self.qtdPortas = qtdPortas

  def imprimirInformacoes(self):
    print(' CARRO - Marca: {}  - Numero rodas: {} - '
          'Modelo: {} - Potencia do motor: {}  - Número portas: {}'
          .format(self.marca, self.qtdRodas, self.modelo, 
                  self.potMotor, self.qtdPortas))