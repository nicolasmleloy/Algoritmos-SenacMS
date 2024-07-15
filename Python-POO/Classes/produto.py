class Produto:
    def __init__(self, marca, nome, desc, preco):
        self.marca = marca
        self.nome = nome
        self.desc = desc
        self.preco = preco

    def getNome(self):
        return self.nome
    
    def getPreco(self):
        return self.preco