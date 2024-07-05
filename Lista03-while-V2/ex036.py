medias = []
qtd = 0

for i in range(1, 3 + 1):
    print(f"\nAluno {i}")
    nota1 = float(input("Informe sua 1ª nota: "))
    nota2 = float(input("Informe sua 2ª nota: "))
    nota3 = float(input("Informe sua 3ª nota: "))
    nota4 = float(input("Informe sua 4ª nota: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4
    medias.append(media)

for i in medias:
    if(i >= 7):
        qtd += 1
    else:
        continue

print(medias)
print(f"Quantidade de alunos com média maior ou igual a 7: {qtd}")