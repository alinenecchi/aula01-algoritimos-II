class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        area = int(self.altura) * int(self.largura)
        return area

    def imprimir(self):
        print('Altura= {}\nLargura= {}'.format(self.altura, self.largura))


