n = 3
m = 3
matriz = []

for linha in range(n):
    lin = []
    for coluna in range(m):
        lin.append(int(input("Informe o valor: ")))
    matriz.append(lin)

print(matriz)

for linhas in matriz:
    print(linhas)