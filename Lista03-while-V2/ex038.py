qtd = int(input("Informe a qtd de números: "))
i = 0
n = 1

if(qtd > 0):
    while(i <= qtd):
        if(i % n == 0):
            print(f"Não primo: {i}")
        else:
            print(i)
        i += 1
        n += 1

        aaaaa = 