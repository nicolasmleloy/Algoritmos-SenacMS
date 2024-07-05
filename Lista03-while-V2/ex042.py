while(True):
    a = int(input("\nInforme um valor: "))
    
    if(a <= 0):
        break
    else:
        q = a ** 2
        c = a ** 3
        r = a ** 0.5

        print(f"Quadrado = {q}")
        print(f"Cubo = {c}")
        print(f"Raíz quadrada = {r}")