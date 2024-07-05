tupla = (1, 7, 3, 20, 10, 5, 8, 6)
soma = 0

for i in tupla:
    if(i % 2 == 0):
        print(i)
        soma += i
    else:
        continue

print(f"Soma dos pares = {soma}")