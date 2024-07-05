nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura: "))
cpf = input("Informe seu CPF: ")

pessoa = {
    "Nome": nome,
    "Idade": idade,
    "Altura": altura,
    "CPF": cpf
}



print(f"{pessoa['Nome']}, tem {pessoa['Idade']} anos e {pessoa['Altura']} de altura!")