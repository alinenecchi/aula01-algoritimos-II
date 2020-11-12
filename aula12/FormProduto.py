import PySimpleGUI as gui
from Produto import Produto

class FormProduto:
    def __init__(self):
        conteudo = [
            [gui.Text("Nome: ") , gui.Input()],
            [gui.Text("Preço: ") , gui.Input(key = 'txtPreco')],
            [gui.Button("Salvar ")]
        ]
        self.tela = gui.Window("Formulário de Produto").layout(conteudo)

    def show(self):
        self.button, self.valores = self.tela.Read()
        nome = self.valores[0]
        if len(nome) != 0:
            prod = Produto()
            prod.nome = nome
            preco = self.valores['txtPreco']
            preco = float(preco.replace(",", "."))
            prod.preco = preco
            return prod
        else:
            return None
        
    