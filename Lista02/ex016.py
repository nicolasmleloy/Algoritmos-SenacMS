valorHora = 40.50
impostoRenda = 0.11

horasTrab = float(input("Informe a quantidade de horas trabalhadas: "))
sBruto = valorHora * horasTrab
sLiquido = sBruto - (sBruto * impostoRenda)

print(f"Salário líquido = {sLiquido}")