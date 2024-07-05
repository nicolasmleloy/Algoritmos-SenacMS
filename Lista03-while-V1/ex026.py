base = int(input("Informe o valor da base: "))
expo = int(input("Informe o valor do expoente: "))
i = 0
res = 1

while(i < expo):
    res *= base
    i += 1

print(f"{base}^{expo} = {res}")