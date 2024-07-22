class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def play(self):
        print(f"Play no {self.nome}: {self.duracao} 😎")

class Acao(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def explodir(self):
        print("Explodindo!!! 💥")

class Comedia(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def rir(self):
        print("HAHAHAHAH 🤣")

class Terror(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def susto(self):
        print("BUUUUUUH 😨")

if __name__ == "__main__":

    filme01 = Acao("007", "2 horas")
    filme02 = Comedia("Gente Grande", "1:30 min")
    filme03 = Terror("Cemitério maldito", "1:40 min")

    filme01.play()
    filme01.explodir()

    filme02.play()
    filme02.rir()

    filme03.play()
    filme03.susto()