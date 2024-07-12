def soma(*args: int):
    soma = 0
    for numero in args:
        soma += numero
    return soma

res = soma(2, 4, 6, 8, 6, 3, 5)
print(res)