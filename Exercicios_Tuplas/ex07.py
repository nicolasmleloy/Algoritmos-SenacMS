matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soma = 0

for i in matriz:
    for q in range(len(i)):
        soma += i[q]

print(f"R = {soma}")