numeros = []

for i in range(0, 5):
    num = int(input("Informe um número: "))
    numeros.append(num)

print(f"Soma = {sum(numeros)}")

for i in numeros:
    print(i)