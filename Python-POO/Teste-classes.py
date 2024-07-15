"""class Escola:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome} fica na Rua {self.endereco}. Fone: {self.telefone}"

class Estudante:
    def __init__(self, nome, idade: int, nota: float):
        self.nome = nome
        self.idade = idade
        self.nota = nota
    

estudante01 = Estudante("Nícolas", 18, 78)
estudante02 = Estudante("Alek", 55, 100)
escola01 = Escola("Senac", "26 de Agosto", "6799234362")
escola02 = Escola("Adair", "Bandeiras", "67992324351")

print(f"{estudante01.nome} estuda na escola {escola01.__str__()}")

class Veiculo:
    def __init__(self, tipo, marca, modelo, tipoAspiracao, cor, peso):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.tipoAspiracao = tipoAspiracao
        self.cor = cor
        self.peso = peso

    def mostrarEspecs(self):
        return f"O(a) {self.tipo} é um(a) {self.marca} {self.modelo} {self.tipoAspiracao} {self.cor}, possui {self.peso}kg."
    
    def maxSpeed(self):
        velocidade = int(input("Qual a velocidade final: "))
        return f"A velocidade final do {self.marca} {self.modelo} {self.tipoAspiracao} é {velocidade} KM/H! 😎"

tipo = input("Tipo do veículo: ")
marca = input("Marca: ")
modelo = input("Modelo: ")
tipoAspiracao = input("Tipo de aspiração: ")
cor = input("Cor: ")
peso = float(input("Peso: "))
print(str(Veiculo(tipo, marca, modelo, tipoAspiracao, cor, peso).mostrarEspecs()))
print(str(Veiculo(tipo, marca, modelo, tipoAspiracao, cor, peso).maxSpeed()))"""

