a = int(input("Informe um número: "))
i = a
mult = 1
lista = []

while(i > 0):
    lista.append(i)
    mult *= i
    i -= 1

print(f"{a}! = {lista} = {mult}")