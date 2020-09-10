from No import No 
class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        
    def adicionar(self, dado):
        no = No (dado)
        if self.tamanho == 0:
            self.inicio = no 
            self.fim = no
        else:
            self.fim.proximo = no
            self.fim = no
        self.tamanho += 1
        
    def imprimir(self):
        texto = ""
        if self.tamanho == 0:
            texto = "Fila vazia"
        else:
            aux = self.inicio
            while (aux):
                texto = texto + str(aux.dado) + " - "
                aux = aux.proximo
        print(texto)
            
    def remover_inicio(self):
        if self.tamanho == 0:
            print("Fila vazia")
        elif self.tamanho == 1:
            self.inicio = None
            self.fim = None
            self.tamanho -= 1
        else:
            self.inicio = self.inicio.proximo 
            self.tamanho -= 1
            print("Removido com sucesso")
            
    
            