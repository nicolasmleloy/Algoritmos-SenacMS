lista = []
par = []
impares = []

for i in range(0, 20):
    num = int(input("Informe um número: "))
    lista.append(num)
    if(num % 2 == 0):
        par.append(num)
    else:
        impares.append(num)

print(lista)
print(par)
print(impares)