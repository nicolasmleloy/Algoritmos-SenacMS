"""i = 0
soma = 0

while(i < 5):
    try:
        num = int(input("Informe um número: "))
        soma += num
        i += 1
    except:
        print("[ERROOOOOOO]")

print(soma)"""

try:
    n1 = int(input("Informe um número: "))
    n2 = int(input("Informe um número: "))

    if(n2 == 0):
        raise RuntimeError("Divisão por zero!!!!!!!")
    divisao = n1 / n2
    print(divisao)
except RuntimeError as r:
    print(f"[ERRO]: {r}")