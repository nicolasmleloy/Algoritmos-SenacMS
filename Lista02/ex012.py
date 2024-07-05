num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if(num1 > num2):
    print(f"{num1} é maior. A diferença é de: {num1 - num2}")
elif(num2 > num1):
    print(f"{num2} é maior. a diferença é de: {num2 - num1}")