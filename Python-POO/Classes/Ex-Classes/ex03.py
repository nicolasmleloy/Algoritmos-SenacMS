class Aluno:
    def __init__(self, nome, ra, n1: float, n2: float, n3: float, n4: float):
        self.nome = nome
        self.ra = ra
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4

    def mostrarSituacao(self):
        media = (self.n1 + self.n2 + self.n3 + self.n4) / 4
        if(media >= 7):
            print("APROVADO! 😎")
        elif(media >= 5 and media <= 6.9):
            print("EXAME! 😒")
        elif(media < 5):
            print("REPROVADO! 😢")
        else:
            print("Algo de errado ocorreu!")

aluno01 = Aluno("Nícolas", "2335", 7.5, 8, 6.5, 9)
aluno01.mostrarSituacao()