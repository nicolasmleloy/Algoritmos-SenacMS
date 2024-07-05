import random
numAleatorio = int(random.uniform(1, 100))
i = 0

while(True):
    numUsuario = int(input("Tente acertar o número misterioso: "))
    i += 1
    if(numUsuario < numAleatorio):
        print(f"{numUsuario} é MENOR")
    if(numUsuario > numAleatorio):
        print(f"{numUsuario} é MAIOR")
    if(numUsuario == numAleatorio):
        print("--" * 30)
        print(f"NÚMERO MISTERIOSO = {numAleatorio}. ACERTOU EM {i} TENTATIVAS!")
        print("--" * 30)
        break