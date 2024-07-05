lista = []

for i in range(10):
    n = int(input("Informe um número: "))
    lista.append(n)
    i += 1

print(f"Menor = {min(lista)}")
print(f"Maior = {max(lista)}")