matriz = [[1, 2, 11, 13], [4, 15, 16, 60], [7, 8, 19, 200], [20, 100, 5, 3]]
maior = matriz[0][0]
l = 0
c = 0

for linha in range(4):
    for coluna in range(4):
        if(matriz[linha][coluna] > maior):
            maior = matriz[linha][coluna]
            l = linha
            c = coluna
            
print(f"Maior = {maior}. Está na linha {l} e coluna {c}")