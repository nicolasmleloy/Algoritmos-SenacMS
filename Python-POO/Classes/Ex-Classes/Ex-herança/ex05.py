class Pessoa:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print(f"{self.nome} está em negociação... 🤝")

class PessoaFisica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf

    def exibirCpf(self):
        print(f"{self.nome} possui o CPF: {self.cpf}")

class PessoaJuridica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj

    def exibirCnpj(self):
        print(f"{self.nome} possui o CNPJ: {self.cnpj}")

pf01 = PessoaFisica("Nícolas", "67991199758", "nicolasadsjf@gmail.com", "26 de Agosto", "028134935")
pf01.negociar()
pf01.exibirCpf()

pj01 = PessoaJuridica("NE", "6799122144", "NE@gmail.com", "Afonso Pena, 001", "986774356435")
pj01.negociar()
pj01.exibirCnpj()