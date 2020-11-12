import PySimpleGUI as gui

class FormCliente:
    def __init__(self):
        conteudo = [
            [gui.Text("Nome: "), gui.Input(size =(30,0), key = 'textNome')],
            [gui.Checkbox("Aceita receber E-mail ",key='aceitaEmail')],
            [gui.Text("Sexo:  ")],
            [
                gui.Radio("Feminino", "sexo", key="feminino"),
                gui.Radio("Masculino", "sexo", key="masculino"),
                gui.Radio("Não informar", "sexo", key="naoInformar")
            ],
            [gui.Text("Idade: "), gui.Slider(range=(0,150), orientation= "h", default_value=18)],
            [gui.Button("Salvar")]
        ]
        self.tela = gui.Window("Formulário de Cliente").layout(conteudo)

    def show(self):
        self.button, self.valores = self.tela.Read()

form = FormCliente()
form.show()
