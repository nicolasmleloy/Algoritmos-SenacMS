class Passagem:
    def __init__(self, preco, assento):
        self.preco = preco
        self.assento = assento

    def alterarPreco(self, novoPreco):
        self.preco = novoPreco
        print(f"Preço atualizado: {self.preco}")
    
    def escolherAssento(self, assento):
        self.assento = assento
        print(f"Assento escolhido: {self.assento}")

class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito: bool):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def abastecer(self):
        print("Abastecendo... ⛽")


class PassagemAviao(Passagem):
    def __init__(self, preco, assento, portaoDeEmbarque, checkIn: bool):
        super().__init__(preco, assento)
        self.portaoDeEmbarque = portaoDeEmbarque
        self.checkIn = checkIn

    def decolar(self):
        print("Decolando... 🛫")
    
passagemBus01 = PassagemBus(200, "G18", "AOB1345", False)
passagemBus01.alterarPreco(130)
passagemBus01.escolherAssento("B8")
passagemBus01.abastecer()

passagemAviao01 = PassagemAviao(1300, "E21", "F10", True)
passagemAviao01.decolar()