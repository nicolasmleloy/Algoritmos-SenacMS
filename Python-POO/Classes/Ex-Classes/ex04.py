import time

class Conta:
    def __init__(self, nome, cpf, numero, saldo: float):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar(self, qtdDeposito):
        print("Depositando...")
        for i in range(3):
            print(".")
            time.sleep(1)
        self.saldo += qtdDeposito
        print(f"Saldo = {self.saldo}")

    def sacar(self, qtdSaque):
        print("Sacando...")
        for i in range(3):
            print("")
            time.sleep(1)
        self.saldo -= qtdSaque
        print(f"Saldo = {self.saldo}")

    def imprimirSaldo(self):
        print(self.saldo)

conta01 = Conta("Nícolas", "233254356", "4674", 200)
conta01.depositar(100)
conta01.sacar(12)
conta01.imprimirSaldo()