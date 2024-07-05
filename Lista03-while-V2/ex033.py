numeros = [42, 87, 23, 76, 58, 33, 91, 65, 17, 29]

num = int(input("Informe um novo número: "))

if num in numeros:
    print(f"Número {num} encontra-se no vetor!")
else:
    print(f"Número {num} NÃO encontra-se no vetor!")