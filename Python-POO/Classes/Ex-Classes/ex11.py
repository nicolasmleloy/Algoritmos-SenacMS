class NF:
    def __init__(self, numero: int, tipo: str, serie: int, cnpj, razaoSocial, data , valorProduto, icms, frete, ipi, valorTotal = 0):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razaoSocial = razaoSocial
        self.data = data
        self.valorProduto = valorProduto
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valorTotal = valorTotal

    def obterNumero(self):
        return self.numero
    
    def obterDataEmissao(self):
        return self.data
    
    def alterarRazaoSocial(self, novaRazao):
        self.razaoSocial = novaRazao
        return self.razaoSocial
    
    def calcularValorTotal(self):
        impostos = ((self.icms + self.ipi) * self.valorProduto) / 100
        self.valorTotal = self.valorProduto + impostos + self.frete
        return self.valorTotal
    
notaFiscal01 = NF(1234, "Entrada", 1, "3455646723", "Asdgfhdgaatja", "17/08/2012", 100.00, 7, 15, 10)
print(notaFiscal01.obterNumero())
print(notaFiscal01.obterDataEmissao())
print(notaFiscal01.alterarRazaoSocial("Razão Social[...]"))
print(notaFiscal01.calcularValorTotal())