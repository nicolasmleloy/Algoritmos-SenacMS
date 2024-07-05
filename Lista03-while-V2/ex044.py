while(True):
    print("\nAdição (opção 1)")
    print("Subtração (opção 2)")
    print("Multiplicação (opção 3)")
    print("Divisão (opção 4)")
    print("Saída (opção 5)")
    opcao = int(input("Informe uma opcao: "))

    if(opcao == 1):
        print("--" * 15)
        n1 = float(input("Informe um número: "))
        n2 = float(input("Informe outro número: "))

        soma = n1 + n2
        print(f"\n{n1} + {n2} = {soma}")
        print("--" * 15)
    elif(opcao == 2):
        print("--" * 15)
        n1 = float(input("Informe um número: "))
        n2 = float(input("Informe outro número: "))
        
        subtracao = n1 - n2
        print(f"\n{n1} - {n2} = {subtracao}")
        print("--" * 15)
    elif(opcao == 3):
        print("--" * 15)
        n1 = float(input("Informe um número: "))
        n2 = float(input("Informe outro número: "))

        mult = n1 * n2

        print("--" * 15)
        print(f"\n{n1} * {n2} = {mult}")
    elif(opcao == 4):
        print("--" * 15)
        n1 = float(input("Informe um número: "))
        n2 = float(input("Informe outro número: "))

        div = n1 / n2
        print(f"\n{n1} / {n2} = {div}")
        print("--" * 15)
    elif(opcao == 5):
        print("Saindo...")
        break
    else:
        print("Opção inválida!")