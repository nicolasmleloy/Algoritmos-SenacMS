numerosDivisiveis = []

for n in range(1, 10000):
    for i in range(1, 21):
        if(n % i == 0):
            numerosDivisiveis.append(n)

print(numerosDivisiveis)