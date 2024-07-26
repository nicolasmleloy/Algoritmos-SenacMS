class Transporte:
    def __init__(self, capacidade):
        self.capacidade = capacidade


class Terrestre(Transporte):
    def __init__(self, capacidade, qtdRodas):
        super().__init__(capacidade)
        self.qtdRodas = qtdRodas

class Automovel(Terrestre):
    def __init__(self, capacidade, qtdRodas, cor, numPortas, placa):
        super().__init__(capacidade, qtdRodas)
        self.cor = cor
        self.numPortas = numPortas
        self.placa = placa

    def ligarAutomovel(self):
        print("🔥⛽")


class Aquatico(Transporte):
    def __init__(self, capacidade):
        super().__init__(capacidade)
    
class Barco(Aquatico):
    def __init__(self, capacidade, tamanhoVela):
        super().__init__(capacidade)
        self.tamanhoVela = tamanhoVela

    def ligarBarco(self):
        print(f"Ligando barco com vela de {self.tamanhoVela} cm 🚤🌊")

class Lancha(Aquatico):
    def __init__(self, capacidade, marca):
        super().__init__(capacidade)
        self.marca = marca

    def ligarLancha(self):
        print(f"Ligando lancha da {self.marca}🚤🌊🌊")

class Navio(Aquatico):
    def __init__(self, capacidade, tipoDeCarga):
        super().__init__(capacidade)
        self.tipoDeCarga = tipoDeCarga

    def ligarNavio(self):
        print(f"Ligando navio de {self.tipoDeCarga} 🚢🌊")


class Aereo(Transporte):
    def __init__(self, capacidade):
        super().__init__(capacidade)
    
class Aviao(Aereo):
    def __init__(self, capacidade):
        super().__init__(capacidade)

class AviaoMonoMotor(Aereo):
    def __init__(self, capacidade, valorAviao):
        super().__init__(capacidade)
        self.valorAviao = valorAviao

    def voar(self):
        print("Avião mono motor voando...🛬🛬")
    
class AviaoComercial(Aereo):
    def __init__(self, capacidade, valorPassagem):
        super().__init__(capacidade)
        self.valorPassagem = valorPassagem

    def exibirValorPassagem(self):
        print(f"Passagem = R${self.valorPassagem}.💸")

if __name__ in "__main__":
    automovel = Automovel("4 pessoas", 4, "preto", 4, "SMA0101")
    automovel.ligarAutomovel()

    barco = Barco("7 pessoas", 10000)
    barco.ligarBarco()

    lancha = Lancha("2 pessoas", "Jet Ski")
    lancha.ligarLancha()

    navio = Navio("20000 toneladas", "cargeiro")
    navio.ligarNavio()

    aviaoMonoMotor = AviaoMonoMotor("6 pessoas", 5000000)
    aviaoMonoMotor.voar()

    aviaoComercial = AviaoComercial("80 passageiros", 2500)
    aviaoComercial.exibirValorPassagem()