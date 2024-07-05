print("---" * 30)
def hello():
    nome = input("Informe o nome: ")
    print(f"Olá {nome}!")

hello()
hello()
hello()
hello()

print("---" * 30)

def soma():
    n1 = int(input("Informe o número 1: "))
    n2 = int(input("Informe o número 2: "))
    return n1 + n2

print(f"Soma = {soma()}")