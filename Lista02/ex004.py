a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite outro número: "))

if(a < b) and (b < c):
    print(f"Os numeros estão em ordem crescente: {a}, {b}, {c}")
else:
    print("Os numeros NÃO estão em ordem crescente!")