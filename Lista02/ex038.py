peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / (altura**2)

if(imc < 18.5):
    print(f"IMC = {imc}. Abaixo do peso")
elif(imc >= 18.6) and (imc <= 24.9):
    print(f"IMC = {imc}. Saudável")
elif(imc >= 25) and (imc <= 29.9):
    print(f"IMC = {imc}. Peso em excesso")
elif(imc >= 30) and (imc <= 34.9):
    print(f"IMC = {imc}. Obesidade Grau I")
elif(imc >= 35) and (imc <= 39.9):
    print(f"IMC = {imc}. Obesidade Grau II(severa)")
elif(imc >= 40):
    print(f"IMC = {imc}. Obesidade Grau III(mórbida)")