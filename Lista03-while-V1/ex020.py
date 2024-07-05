sair = False
pares = 0
i = 0

while(not sair):
    n = int(input("Informe um número, ou digite 0: "))
    if(n == 0):
        sair = True
    elif(n % 2 == 0):
        print(f"Número {n} é par!")
        pares += 1
    else:
        print(f"Número {n} não é par!")
    i += 1

print("--" * 10)
print(f"Qtd dados lidos = {i-1}")
print(f"Qtd números pares = {pares}")
print("--" * 10)