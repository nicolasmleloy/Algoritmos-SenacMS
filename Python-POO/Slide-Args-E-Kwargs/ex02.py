def media(*numeros):
    try:
        soma = 0
        for n in numeros:
            soma += n
        media = soma / len(numeros)
        return media
    except TypeError:
        print("[Erro]: Tipo incorreto!")

res = media(5.5, 8.6, 9.3, 10, 7.5)
print(f"{res:.2f}")