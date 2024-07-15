class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def mostrarNome(self):
        return self.nome
    
    def alterarIdade(self, novaIdade):
        self.idade = novaIdade
        return novaIdade

    def imprimirEndereco(self):
        return self.endereco
    
pessoa01 = Pessoa("Nícolas", 18, "26 de agosto")
print(pessoa01.mostrarNome())
print(pessoa01.alterarIdade(19))
print(pessoa01.imprimirEndereco())