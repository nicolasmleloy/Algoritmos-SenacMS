class Funcionario:
    def __init__(self, nome, sobrenome, horasTrab, valorHora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horasTrab = horasTrab
        self.valorHora = valorHora

    def nomeCompleto(self):
        print(f"{self.nome} {self.sobrenome}")
    
    def calcularSalario(self):
        salario = self.horasTrab * self.valorHora
        print(f"Salário = {salario}")
    
    def incrementarHoras(self, incremento):
        self.valorHora += incremento
        salario = self.horasTrab * self.valorHora
        print(f"Salário incrementado = {salario}")

func01 = Funcionario("Nícolas", "Marcelo Lima Eloy", 60, 20)
func01.nomeCompleto()
func01.calcularSalario()
func01.incrementarHoras(10)