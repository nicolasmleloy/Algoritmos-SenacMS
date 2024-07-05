n = int(input("Informe um número entre 100 e 9999: "))
i = 0

if(n >= 100) and (n <= 9999):
    n = str(n)
    while(i < len(n)):
        print(n[i])
        i += 1