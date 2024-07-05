a = float(input("Informe um valor: "))
b = float(input("Informe outro valor: "))
c = float(input("Informe outro valor: "))

if(a < b + c) and (b < a + c) and (c < a + b):
    if(a == b) and (a == c):
        print("Triângulo equilátero!")
    elif(a == b) or (b == c) or (a == c):
        print("Triângulo isóceles!")
    elif(a != b) and (a != c):
        print("Triângulo escaleno!")