n = int(input("Informe número par: "))
i = 0

if(n >= 0):
    if(n % 2 == 0):
        while(i <= n):
            if(i % 2 == 0):
                print(i)
            i += 1
    else:
        print("Número deve ser par!")
else:
    print("Número não inteiro positivo!")