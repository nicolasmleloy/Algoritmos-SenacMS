class Imovel:
    def __init__(self, inscricaoMun, valorAluguel, iptu):
        self.inscricaoMun = inscricaoMun
        self.valorAluguel = valorAluguel
        self.iptu = iptu

    def obterParcelaIptu(self):
        for i in range(1, 13):
            print(f"Valor = R${self.valorAluguel / i:.2f}, {i}x")
        
    def setValorAluguel(self, novoValor):
        self.valorAluguel = novoValor
        print(f"Novo valor = {self.valorAluguel}")
    
class Casa(Imovel):
    def __init__(self, inscricaoMun, valorAluguel, iptu, piscina: bool, churrasqueira: bool, qtdBanheiro, qtdQuartos):
        super().__init__(inscricaoMun, valorAluguel, iptu)
        self.piscina = piscina
        self.currasqueira = churrasqueira
        self.qtdBanheiro = qtdBanheiro
        self.qtdQuartos = qtdQuartos

    def calcularM2(self, frente, lateral):
        area = frente * lateral
        print(f"Área = {area}m2")

class Apartamento(Imovel):
    def __init__(self, inscricaoMun, valorAluguel, iptu, qtdAndares, areaLazer: bool, elevador: bool):
        super().__init__(inscricaoMun, valorAluguel, iptu)
        self.qtdAndares = qtdAndares
        self.areaLazer = areaLazer
        self.elevador = elevador

    def mostrarQualidades(self):
        if(self.areaLazer == True and self.elevador == True):
            print("Possui área de lazer e elevador!")
        else:
            print("Não possui muitas qualidades.")
    
class Terreno(Imovel):
    def __init__(self, inscricaoMun, valorAluguel, iptu, largura, comprimento):
        super().__init__(inscricaoMun, valorAluguel, iptu)
        self.area = largura * comprimento

    def exibirArea(self):
        print(f"Área = {self.area}m2")


class Chacara(Imovel):
    def __init__(self, inscricaoMun, valorAluguel, iptu, largura, comprimento):
        super().__init__(inscricaoMun, valorAluguel, iptu)
        self.hectares = (largura * comprimento) / 10000

    def exibirHectares(self):
        print(f"A chácara possui {self.hectares} hectares")

if __name__ == "__main__":
    inscricaoMun = input("Informe a inscrição municipal: ")
    valorAluguel = float(input("Informe o valor do aluguel: "))
    iptu = float(input("Informe o valor do iptu: "))

    casa = Casa(inscricaoMun, valorAluguel, iptu, False, True, 2, 3)
    ap = Apartamento(inscricaoMun, valorAluguel, iptu, 10, True, True)
    terreno = Terreno(inscricaoMun, valorAluguel, iptu, 30, 50)
    chacara = Chacara(inscricaoMun, valorAluguel, iptu, 500, 1000)

    print("\n---------------")
    casa.calcularM2(20, 40)
    casa.obterParcelaIptu()
    print("---------------\n")
    ap.mostrarQualidades()
    print("\n---------------")
    terreno.exibirArea()
    print("---------------\n")
    chacara.exibirHectares()
    print("\n---------------")