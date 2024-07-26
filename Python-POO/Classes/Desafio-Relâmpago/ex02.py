class Forma:
    def __init__(self, nome):
        self.nome = nome

    def descicao(self):
        print(self.nome)

class Quadrado(Forma):
    def __init__(self, nome, lado: float):
        super().__init__(nome)
        self.lado = lado

    def nomeEComprimento(self, lado):