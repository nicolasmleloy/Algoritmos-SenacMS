print("--" * 20)
print("1 - Para adição: ")
print("2 - Para subtração: ")
print("3 - Para multiplicação: ")
print("4 - Para divisão: ")
print("--" * 20)
opcao = int(input("Escolha uma operação acima: "))

if(opcao == 1):
    num1 = float(input("Digite um número para a operação: "))
    num2 = float(input("Digite outro número para a operação: "))

    print(f"Soma entre {num1} e {num2} = {num1 + num2}")
elif(opcao == 2):
    num1 = float(input("Digite um número para a operação: "))
    num2 = float(input("Digite outro número para a operação: "))

    print(f"Subtração entre {num1} e {num2} = {num1 - num2}")
elif(opcao == 3):
    num1 = float(input("Digite um número para a operação: "))
    num2 = float(input("Digite outro número para a operação: "))

    print(f"Multiplicação entre {num1} e {num2} = {num1 * num2}")
elif(opcao == 4):
    num1 = float(input("Digite um número para a operação: "))
    num2 = float(input("Digite outro número para a operação: "))

    print(f"Divisão entre {num1} e {num2} = {num1 / num2}")
else:
    print("Opção inválida!")