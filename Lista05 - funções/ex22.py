def criaMatriz():
    matriz = []
    for l in range(4):
        l = []
        for c in range(4):
            num = int(input("Informe um número: "))
            l.append(num)
        matriz.append(l)

    return matriz

def criaMatrizUser(linha):
    matriz = criaMatriz()

    for m in matriz:
        print(m)
    print(f"Soma = {sum(matriz[linha])}")

criaMatrizUser(0)