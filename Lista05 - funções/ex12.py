def somaEntreNumeros(a, b):
    soma = 0
    for numero in range(a, b + 1):
        soma += numero

    return soma

print(somaEntreNumeros(10, 20))