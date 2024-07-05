try:
    num = int(input("Informe um número: "))
    print(type(num))
except ValueError:
    print("[ERRO] Value error")