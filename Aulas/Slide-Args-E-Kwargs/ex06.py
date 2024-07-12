def media(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    media = soma / len(numeros)
    return media

res = media(7.1, 36.2, 92.3, 96.4, 103.5, 702.6)
print(f"{res:.2f}")