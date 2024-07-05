caracteres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
qtd = 0

for i in caracteres:
    if(i != "a" and i != "e" and i != "i" and i != "o" and i != "u"):
        print(i)
        qtd += 1
    else:
        continue

print(f"Quantidade de consoantes: {qtd}")