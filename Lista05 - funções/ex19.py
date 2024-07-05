import random

numeros = []

def sorteia():
    for i in range(5):
        numero = random.randint(0, 100)
        numeros.append(numero)

def somaPar():
    sorteia()
    print(numeros)
    soma = 0
    for numero in numeros:
        if(numero % 2 == 0):
            soma += numero
            print(numero)
    return soma

print(f"Soma = {somaPar()}")