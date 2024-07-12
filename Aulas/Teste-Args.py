"""def worldCupTitles(pais, *args):
    print(f"País: {pais}", end=" ")
    for anos in args:
        print(f"{anos}", end=", ")

worldCupTitles("Brasil", "1950", "1962", "1970", "1994", "2002")

def pessoa(**kwargs):
    for i in kwargs:
        print(kwargs[i])

pessoa(nome = "Nícolas", idade = 18, altura = 1.85, peso = 60)"""

def dadosPessoais(**dados):
    print("--" * 15)
    for d in dados:
        print(f"{d} é {dados[d]}")
    print("--" * 15)
    
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Infrome sua altura: "))

dadosPessoais(Nome = nome, Idade = idade, Altura = altura)