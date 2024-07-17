class AlunoAcademia:
    def __init__(self, nome, idade, peso, altura, mensalidade = 120.00):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def maiorOuMenor(self):
        if(self.idade >= 18):
            return "Maior"
        else:
            return "Menor"
        
    def calcularImc(self):
        res = self.peso / self.altura ** 2
        print(f"IMC = {res:.2f}")

    def obterValorMensalidade(self):
        if(self.maiorOuMenor() == "Menor"):
            desconto = self.mensalidade * 0.10
            self.mensalidade -= desconto
        print(self.mensalidade)

aluno01 = AlunoAcademia("Nícolas", 15, 60, 1.87, 85.00)
print(aluno01.maiorOuMenor())
aluno01.calcularImc()
aluno01.obterValorMensalidade()