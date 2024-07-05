def criaMatriz(linha, coluna):
    matriz = []
    for l in range(linha):
        linha = []
        for c in range(coluna):
            linha.append(1)
        matriz.append(linha)

    return matriz

matriz = criaMatriz(3, 3)
for m in matriz:
    print(m)