a = int(input("Informe um numero para COMEÇAR: "))
b = int(input("informe um número para TERMINAR: "))
i = a
soma = 0

if(a < b):
    while(i <= b):
        if(i % 2 == 1):
            soma += i
        i += 1
    print(f"Soma = {soma}")
else:
    print("Itervalo de valores inválido")
    exit()