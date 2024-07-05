def triangulo(n):
    base = 2 * n - 1
    for i in range(base):
        for j in range(base-i-1):
            print(" ", end="")
        for k in range(i+1):
            print("* ", end="")
        print()

triangulo(6)