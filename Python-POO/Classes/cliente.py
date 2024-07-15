class Cliente:
    def __init__(self, cpf: str, nome: str, idade: int):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade

    def getNome_Idade(self):
        return self.nome, self.idade #RETORNA UMA TUPLA
    
    def getCpf(self):
        return self.cpf