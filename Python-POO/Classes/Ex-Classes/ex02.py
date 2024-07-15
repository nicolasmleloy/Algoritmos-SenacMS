class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterarEditora(self, novaEditora) -> str:
        self.editora = novaEditora
        print(novaEditora)
    
    def listarQtdPag(self):
        print(self.paginas)
    
livro01 = Livro("O anel do anão", "Nícolas", "Nícolas Edições", 322)
livro01.alterarEditora("Nícolas Produções")

livro01.listarQtdPag()