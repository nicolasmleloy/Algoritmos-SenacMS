class Funcionario:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario

    def baterPonto(self):
        print(f"{self.nome} bateu ponto! ✅")


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, senha, definirMeta: float):
        super().__init__(nome, matricula, salario)
        self.senha = senha
        self.definirMeta = definirMeta

    def confirmarSenha(self):
        confirmar = input("Confirme sua senha: ")
        while(confirmar != self.senha):
            confirmar = input("Senha incorreta, tente novamente: ")
        print("Correto! ✅")


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao: float):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao

    def bateuMeta(self, metaDefinida):
        if(self.comissao > metaDefinida):
            print(f"R${self.comissao} de comissão. Bateu a meta! 🎉")
        else:
            print(f"R${self.comissao} de comissão. Não bateu a meta! 😢")


gerente = Gerente("Alek", "0987", 10500, "123456", 1500)
vendedor01 = Vendedor("Nícolas", "0123", "5500", 2000)
vendedor01.bateuMeta(gerente.definirMeta)
vendedor01.baterPonto()

gerente.baterPonto()
gerente.confirmarSenha()