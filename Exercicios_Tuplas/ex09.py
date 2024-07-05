matriz = [[1, 2, 11, 13], [4, 15, 16, 60], [7, 8, 19, 200], [20, 100, 5, 3]]
maior = matriz[0][0]
qtd = 0

for linha in matriz:
    for coluna in range(4):
        if(linha[coluna] > 10):     
            qtd += 1
        else:
            continue

print(f"R = {qtd}")