n = int(input("Informe um número: "))
i = 1
soma = 0

while(i < n):
    if(n % i == 0):
        soma += i
        print(i)
    i += 1

print(f"Soma = {soma}")