altura = float(input("Informe sua altura: "))
sexo = input("Informe o seu sexo: ")

if(sexo == "Masculino") or (sexo == "M"):
    pesoIdeal = (72.7 * altura) - 58
    print(f"Peso ideal = {pesoIdeal}")
elif(sexo == "Feminino") or (sexo == "F"):
    pesoIdeal = (62.1 * altura) - 44.7
    print(f"Peso ideal = {pesoIdeal}")