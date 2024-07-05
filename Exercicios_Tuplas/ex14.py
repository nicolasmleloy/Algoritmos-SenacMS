a = [[1, 13, 3], [4, 45, 67], [7, 80, 9]]
b = [[100, 8, 7], [6, 5, 4], [3, 25, 10]]
soma = 0

for linha in range(3):
    l = []
    for coluna in range(3):
        soma = a[linha][coluna] + b[linha][coluna]
        l.append(soma)
    print(l)