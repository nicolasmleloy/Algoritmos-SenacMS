class Ingresso:
    def __init__(self, preco, setor):
        self.preco = preco
        self.setor = setor

    def alterarPreco(self, novoPreco):
        self.preco = novoPreco
        print(f"Preço atualizado: R${self.preco}")

    def mostrarSetor(self):
        print(f"Setor: {self.setor}")

class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote: bool, openBar: bool, openFood: bool, estacionamento: bool):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.openBar = openBar
        self.openFood = openFood
        self.estacionamento = estacionamento

    def pegarBebida(self):
        print("Pegando bebida... 🍺")

    def acessarCamarote(self):
        print("Acessando camarote... 😎")

ingresso01 = IngressoVIP(150, "Leste", True, True, True, False)
ingresso01.alterarPreco(100)
ingresso01.mostrarSetor()
ingresso01.pegarBebida()
ingresso01.acessarCamarote()