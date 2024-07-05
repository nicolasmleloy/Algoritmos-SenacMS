n = int(input("Informe um número: "))
i = 2

if(n > 1):
    while(i < n):
        if(n % i == 0):
            print(f"Número {n} não é primo!")
            break
        else:
            print(f"Número {n} é primo!")
            print(i)
        i += 1
else:
    print("Número inválido!")