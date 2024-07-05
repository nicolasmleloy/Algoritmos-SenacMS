print("--" * 20)
print("1 - Soma de 2 números: ")
print("2 - Diferença entre 2 números: ")
print("3 - Produto entre 2 núemeros: ")
print("4 - Divisão entre 2 números: ")
print("--" * 20)
opcao = int(input("Escolha uma operação acima: "))

if(opcao == 1):
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    print(f"Soma entre {num1} e {num2} = {num1 + num2}")
elif(opcao == 2):
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    if(num1 > num2):
        print(f"Diferença entre {num1} e {num2} = {num1 - num2}")
    else:
        print(f"Diferença entre {num1} e {num2} = {num2 - num1}")
elif(opcao == 3):
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    print(f"Produto entre {num1} e {num2} = {num1 * num2}")
elif(opcao == 4):
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    if(num1 <= 0) or (num2 <= 0):
        print("Denominador inválido!")
    else:
        print(f"Divisão entre {num1} e {num2} = {num1 / num2}")
else:
    print("Opção inválida!")