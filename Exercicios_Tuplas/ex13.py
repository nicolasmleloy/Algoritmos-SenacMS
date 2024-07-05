matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soma = 0

for linha in range(3):
    for coluna in range(3):
        if(linha == coluna):
            soma += matriz[linha][coluna]
            
print(soma)