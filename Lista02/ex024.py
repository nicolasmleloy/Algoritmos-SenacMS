baseMenor = float(input("Informe o tamanho da base menor: "))
baseMaior = float(input("Informe o tamanho da base maior: "))
altura = float(input("Informe o tamanho da altura: "))

if(baseMaior >= 0) and (baseMenor >= 0):
    area = ((baseMaior + baseMenor) * altura) / 2
    print(f"Área do trapézio = {area}")
else:
    print("Valor de base maior e base menor inválidos!")