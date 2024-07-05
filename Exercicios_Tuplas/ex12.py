matriz = [[1, 120, -3], [2, 5, 250], [7, 0, 9]]
maior = matriz[0][0]
menor = matriz[0][0]
l1 = 0
c1 = 0
l2 = 0
c2 = 0

for linha in range(3):
    for coluna in range(3):
        if(matriz[linha][coluna] > maior):
            maior = matriz[linha][coluna]
            l1 = linha
            c1 = coluna
        elif(matriz[linha][coluna] < menor):
            menor = matriz[linha][coluna]
            l2 = linha
            c2 = coluna
            
print(f"Maior = {maior}. Está na linha {l1} e coluna {c1}")
print(f"Menor = {menor}. Está na linha {l2} e coluna {c2}")