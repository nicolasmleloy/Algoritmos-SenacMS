num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if(num1 > num2):
    inverte1 = num1 - (num1 - num2)
    inverte2 = num2 + (num1 - num2)
    print(inverte1)
    print(inverte2)
else:
    inverte1 = num1 + (num2 - num1)
    inverte2 = num2 - (num2 - num1)
    print(inverte1)
    print(inverte2)