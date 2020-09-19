from node import Node
#inserir no fim da pilha 
#remover elemento que está no topo da pilha 
#observar o topo da pilha 

class Pilha:
    def __init__(self):
        self.topo = None 
        self.tamanho = 0
        
    def inserir(self, novo_dado):
        novo_node = Node(novo_dado)
        novo_node.anterior = self.topo
        self.topo = novo_node
        self.tamanho = self.tamanho + 1
        
    def remover(self):
        assert self.topo,"Impossível remover valor de Pilha vazia"
        self.topo = self.topo.anterior
        self.tamanho = self.tamanho - 1
    
    def __repr__(self):
        return str(self.topo) + '->Tamanho da pilha: ' + str(self.tamanho)
   

    