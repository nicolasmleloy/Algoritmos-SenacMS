a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

if(a > 0):
    delta = b**2 - (4 * a * c)
    if(delta < 0):
        print("Não existe raíz")
    elif(delta == 0):
        print("Raíz única")
    elif(delta >= 0):
        x1 = (-b + delta**0.5) / (2 * a)
        x2 = (-b - delta**0.5) / (2 * a)
        equacao1 = a*(x1**2) + b * x1 + c == 0
        equacao2 = a*(x2**2) + b * x2 + c == 0

        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
        print(f"Equacão 1 = {equacao1} || Equação 2 = {equacao2}")
else:
    print("Não é equação de segundo grau.")