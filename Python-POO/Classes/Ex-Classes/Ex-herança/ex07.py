class Brinquedo:
    def __init__(self, nome, cor, tamanho, preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f"Estou brincando com {self.nome} {self.cor}")

class Ben10(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, tranformado: bool):
        super().__init__(nome, cor, tamanho, preco)
        self.transformado = tranformado

    def estaTransformado(self):
        if(self.transformado == True):
            print(f"{self.nome} está transformado!")
        else:
            print(f"{self.nome} está normal.")
    
class Chaves(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, feliz: bool):
        super().__init__(nome, cor, tamanho, preco)
        self.feliz = feliz

    def estaFeliz(self):
        if(self.feliz == True):
            print("Isso! Isso! Isso! Isso!")
        else:
            print("Pi Pi Pi Pi Pi Pi Pi Pi")

class Kiko(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, bravo: bool):
        super().__init__(nome, cor, tamanho, preco)
        self.bravo = bravo

    def estaBravo(self):
        if(self.bravo == True):
            print("Gentália Gentália Gentália Gentália")
        else:
            print("😊⚽ 😊⚽ 😊⚽")

class SrMadruga(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, trabalha: bool):
        super().__init__(nome, cor, tamanho, preco)
        self.trabalha = trabalha

    def estaTrabalhando(self):
        if(self.trabalha == True):
            print(f"{self.nome} trabalha 🤑")
        else:
            print(f"{self.nome} não trabalha 😢")
    
class SrBarriga(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, imovel: True):
        super().__init__(nome, cor, tamanho, preco)
        self.imovel = imovel

    def possuiImovel(self):
        if(self.imovel == True):
            print(f"{self.nome} está rico 💸")
        else:
            print(f"{self.nome} está pobre 😥")

if __name__ == "__main__":
    ben10 = Ben10("Ben 10", "verde", "realista", 100, True)
    chaves = Chaves("Chaves", "branco", "realista", 120, False)
    kiko = Kiko("Kiko", "branco", "realista", 120, True)
    srMadruga = SrMadruga("Sr. Madruga", "branco", "realista", 90, False)
    srBarriga = SrBarriga("Sr. Barriga", "branco", "realista", 110, True)

    print("\n")
    ben10.brincar()
    ben10.estaTransformado()

    print("\n")
    chaves.brincar()
    chaves.estaFeliz()

    print("\n")
    kiko.brincar()
    kiko.estaBravo()

    print("\n")
    srMadruga.brincar()
    srMadruga.estaTrabalhando()

    print("\n")
    srBarriga.brincar()
    srBarriga.possuiImovel()