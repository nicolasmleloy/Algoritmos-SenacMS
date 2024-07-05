qtd_numeros = int(input("Informe a quantidade de números: "))
numeros = []
i = 0

while(i < qtd_numeros):
    n = int(input("Informe um número: "))
    numeros.append(n)
    i += 1

print(max(numeros))