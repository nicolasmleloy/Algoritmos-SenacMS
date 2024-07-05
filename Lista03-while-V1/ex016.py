n = int(input("Informe número ímpar: "))
i = 1

if(n >= 0):
    if(n % 2 == 1):
        while(i <= n):
            if(i % 2 == 1):
                print(i)
            i += 1
    else:
        print("Número deve ser ímpar!")
else:
    print("Número não inteiro positivo!")