nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))

if(nota1 >= 0.0) and (nota1 <= 10.0) and (nota2 >= 0.0) and (nota2 <= 10.0):
    media = (nota1 + nota2) / 2
    print(f"Média = {media}")
else:
    print("valor inválido!")