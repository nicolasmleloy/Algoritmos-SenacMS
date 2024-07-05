numeros = []

while(True):
    num = int(input("Informe um número: "))
    if(num < 0 ):
        break
    numeros.append(num)


print(f"\nMenor número: {min(numeros)}")
print(f"Maior número: {max(numeros)}")