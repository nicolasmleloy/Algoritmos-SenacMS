class Pessoa:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, b1, b2, b3, b4):
        super().__init__(matricula, nome, idade)
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.media = (self.b1 + self.b2 + self.b3 + self.b4) / 4

    def estudar(self):
        print(f"Aluno {self.nome} está estudando! 🤓")

    def mostrarMedia(self):
        print(f"Média do aluno: {self.nome} = {self.media:.1f}")
    
class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, ch, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.ch = ch
        self.salario = salario

    def lecionar(self):
        print(f"Professor(a) {self.nome} de {self.disciplina} está lecionando! 📚")
    
aluno01 = Aluno("012121", "Nícolas", 18, 8, 9, 4.5, 6)
profrssor01 = Professor("01313131", "Alek garai", 35, "letras", "Inglês", 500, 1500000)

aluno01.estudar()
aluno01.mostrarMedia()
profrssor01.lecionar()