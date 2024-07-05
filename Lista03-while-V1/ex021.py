num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))
soma = 0
mult = 1

for i in range(num1, num2+1):
    if(i % 2 == 0):
        soma += i
        print(f"P = {i}")
    else:
        mult *= i
        print(f"I = {i}")

print(f"Soma = {soma + num1 + num2}")
print(f"Multiplicação = {mult * num1 * num2}")