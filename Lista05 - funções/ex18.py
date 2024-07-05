def triangulo(n):
    for i in range(n + 1):
        print("*" * i)
    for a in range(n - 1, 0, -1):
        print("*" * a)

triangulo(4)