nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))

nota3 *= 2

media = (nota1 + nota2 + nota3) / 5

if(media >= 60):
    print(f"média = {media:.2f}. Aprovado!")
else:
    print(f"média = {media:.2f}. Reprovado!")