def media(letra, n1, n2, n3):
    if(letra == "A"):
        media = (n1 + n2 + n3) / 3
    elif(letra == "P"):
        media = ((5 * n1) + (3 * n2) + (2 * n3)) / (5 + 3 + 2)
    else:
        print("Letra inválida!")

    return media

print(media("P", 7, 9, 10))