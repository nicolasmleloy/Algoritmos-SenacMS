class Agenda:
    def __init__(self, dia, mes, ano, anotacao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def validarData(self):
        print(self.dia, self.mes, self.ano, sep="/")

    def anotarTarefa(self):
        self.anotacao = input("Faça sua anotação: ")
    
    def mostrarAnotacao(self):
        print(f"Sua anotação: {self.anotacao}")

agenda01 = Agenda("17", "08", "2005", "Hello, world! This is my writing. Thank you, Nícolas.")
agenda01.validarData()
agenda01.anotarTarefa()
agenda01.mostrarAnotacao()