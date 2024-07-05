valorHora = float(input("Informe o valor da hora: "))
horasTrab = float(input("Informe a quantidade de horas trabalhadas: "))
impRenda = 0.11
inss = 0.08
sindicato = 0.05

salario = valorHora * horasTrab
print(f"Salário bruto = R${salario}")
print(f"Pago ao INSS = R${salario * impRenda}")
print(f"Pago ao sindicato = R${salario * sindicato}")
print(f"Salário liquido = R${salario - ((salario * impRenda) + (salario * inss) + (salario * sindicato))}")