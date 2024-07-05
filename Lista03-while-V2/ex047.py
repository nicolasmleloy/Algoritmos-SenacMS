quadradoSoma = 0
quadrado = 0
soma = 0
i = 1

while(i <= 100):
    quadrado = i ** 2
    soma += quadrado
    quadradoSoma += i
    i += 1

quadradoSoma = quadradoSoma ** 2
print(f"Soma = {soma}")
print(f"Quadrado soma = {quadradoSoma}")
print(f"Diferença = {quadradoSoma - soma}")