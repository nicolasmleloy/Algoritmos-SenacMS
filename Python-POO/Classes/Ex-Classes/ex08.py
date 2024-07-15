class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcularPerimetro(self):
        res = self.ladoA + self.ladoB + self.ladoC
        print(f"Perímetro = {res}")

    def getMaiorLado(self):
        maior = self.ladoA
        if(self.ladoB > maior):
            maior = self.ladoB
        if(self.ladoC > maior):
            maior = self.ladoC
        print(f"Maior = {maior}")

ladoA = int(input("Informe o lado A: "))
ladoB = int(input("Informe o lado B: "))
ladoC = int(input("Informe o lado C: "))

triangulo01 = Triangulo(ladoA, ladoB, ladoC)
triangulo01.calcularPerimetro()
triangulo01.getMaiorLado()