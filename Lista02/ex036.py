salario = float(input("Informe o salário: "))
tempoServico = int(input("Informe o tempo de serviço na empresa em anos: "))

if(salario <= 500):
    reajuste = (salario * 0.25)
    print(f"Salário final reajustado = {salario + reajuste} reais. Sem bônus!")
elif(salario < 1000):
    reajuste = (salario * 0.20)
    print(f"Salário final reajustado = {salario + reajuste} reais.")

    if(tempoServico >= 1) and (tempoServico <= 3):
        bonus = salario + 300
        print(f"Salário com bônus = {(salario + reajuste) + bonus}")

elif(salario < 1500):
    reajuste = (salario * 0.15)
    print(f"Salário final reajustado = {salario + reajuste} reais.")

    if(tempoServico >= 4) and (tempoServico <= 6):
        bonus = salario + 200
        print(f"Salário com bônus = {(salario + reajuste) + bonus}")

elif(salario < 2000):
    reajuste = (salario * 0.10)
    print(f"Salário final reajustado = {salario + reajuste} reais.")

    if(tempoServico >= 7) and (tempoServico <= 10):
        bonus = salario + 300
        print(f"Salário com bônus = {(salario + reajuste) + bonus}")

elif(salario > 20000):
    print("Sem reajuste.")

    if(tempoServico > 10000):
        bonus = salario + 500
        print(f"Salário com bônus = {salario + bonus}")