class Compra:
    def __init__(self, numero, produto, valor, valorTotal = 0):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valorTotal = valorTotal

    def calcularValorTotal(self):
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        self.valorTotal = self.valor + icms + frete
        return self.valorTotal

class AVista(Compra):
    def __init__(self, numero, produto, valor, desconto, valorTotal=0):
        super().__init__(numero, produto, valor, valorTotal)
        self.desconto = desconto

    def precoComDesconto(self):
        valorTotal = Compra.calcularValorTotal(self)
        desconto = valorTotal * self.desconto / 100
        res = valorTotal - desconto
        print(f"\nValor total com desconto = R${res}\n")
    
class Parcelado(Compra):
    def __init__(self, numero, produto, valor, qtdParc, valorTotal=0):
        super().__init__(numero, produto, valor, valorTotal)
        self.qtdParc = qtdParc

    def exibirParcelas(self):
        valorTotal = Compra.calcularValorTotal(self)
        for p in range(1, 13):
            print(f"Parcela valor total = R${valorTotal / p:.2f}, {p}x")

compra01 = AVista("0123", "Tênis", 350.00, 10)
compra01.precoComDesconto()

compra02 = Parcelado("04321", "Camiseta", 100.00, 8)
compra02.exibirParcelas()