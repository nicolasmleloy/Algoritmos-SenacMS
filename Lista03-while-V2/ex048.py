lista = [17, 8, 26, 17, 33, 8, 42, 26, 50, 17, 8, 26, 33, 17, 8, 42, 26, 50, 17, 8]
i = lista[0]
qtdN1 = 0
qtdN2 = 0
qtdN3 = 0

n1 = int(input("Informe um número: "))
n2 = int(input("Informe um número: "))
n3 = int(input("Informe um número: "))

while(i < len(lista)):
    if(i == n1):
        qtdN1 += 1
    if(i == n2):
        qtdN2 += 1
    if(i == n3):
        qtdN3 += 1
    i += 1
    print(i)

print(f"{n1}: ocorreu {qtdN1} vezes")
print(f"{n2}: ocorreu {qtdN2} vezes")
print(f"{n3}: ocorreu {qtdN3} vezes")