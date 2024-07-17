class Carro:
    def __init__(self, marca, modelo, cor, ano, valor, consumo, nivelComb = 5):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo
        self.nivelComb = nivelComb

    def ligar(self):
        a = int(input("Digite 1 para ligar o carro: "))
        while(a != 1):
            if(a != 1):
                a = int(input("O carro ainda está desligado, digite 1 para ligar: "))
            else:
                a = int(input("Digite 1 para ligar o carro: "))

        print("Carro ligado! 😎🚗")
    
    def abastecer(self, qtd):
        self.nivelComb += qtd
        print(f"Nível = {self.nivelComb}")
    
    def andar(self, distancia):
        print(f"Distancia percorrida: {distancia} km.")

    def verificarNivel(self, distancia):
        res = self.nivelComb / distancia
        print(f"{res} litros gastos por km.")

    def calcularImposto(self):
        ipva = (self.valor * 2.5) / 100
        print(f"IPVA = R${ipva}")

carro01 = Carro("Volkswagen", "Gol", "Preto", 2014, 90000, 12, 100)
carro01.ligar()
carro01.abastecer(40)
carro01.andar(10)
carro01.verificarNivel(120)
carro01.calcularImposto()