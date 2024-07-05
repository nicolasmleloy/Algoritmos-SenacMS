i = 0
positivo = 0
soma = 0

while(i < 10):
    n = int(input("Informe um número: "))
    if(n > 0):
        soma += n
        positivo += 1
    i += 1

print(f"Média = {soma / positivo}")