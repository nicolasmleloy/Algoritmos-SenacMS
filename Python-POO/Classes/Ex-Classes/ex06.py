class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def imprimirRaio(self):
        print(self.raio)

    def calcArea(self):
        res = 3.1415 * self.raio ** 2
        print(f"Área = {res}")

    def calcCircunferencia(self):
        res = 2 * 3.1415 * self.raio
        print(f"Circunferência = {res}")
    
circulo01 = Circulo(5)
circulo01.imprimirRaio()
circulo01.calcArea()
circulo01.calcCircunferencia()