class Triangulo:
    def __init__(self, *lados):
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
        return maior

class Medidas(Triangulo):
    def __init__(self, *lados):
        super().__init__(*lados)

    def imprimirArea(self, base, altura):
        res = (base * altura) / 2
        print(f"Área = {res}")

    def maiorLado(self):
        print(f"Maior lado = {self.getMaiorLado()}")

lados = []

for i in range(1, 4):
    print(f"\nTriangulo {i}\n")

    ladoA = int(input("Informe o lado A: "))
    ladoB = int(input("Informe o lado B: "))
    ladoC = int(input("Informe o lado C: "))

    lados.append(ladoA)
    lados.append(ladoB)
    lados.append(ladoC)

    triangulo = Triangulo(lados)
    triangulo.calcularPerimetro()
    triangulo.getMaiorLado()
    triangulo = Medidas(lados)
    triangulo.imprimirArea(2, 4)
    triangulo.maiorLado()