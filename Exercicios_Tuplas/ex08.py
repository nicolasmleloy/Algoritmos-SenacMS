matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for linha in matriz:
    l = []
    for coluna in range(len(linha)):
        l.append(linha[coluna])
    print(l)