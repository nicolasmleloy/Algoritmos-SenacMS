n = int(input("Informe um número: "))
i = 0
soma = 0

if(n >= 0):
    while(i < n):
        i += 1
        soma += i

    print(soma)
else:
    print("Número não inteiro positivo!")