salarioC = float(input("Informe o salário de Carlos: "))
salarioJ = salarioC / 3
meses = 0
rendimentoTotalC = salarioC
rendimentoTotalJ = salarioJ

while(rendimentoTotalC > rendimentoTotalJ):
    rendimentoMesC = 0.02 * rendimentoTotalC
    rendimentoTotalC += rendimentoMesC
    
    rendimentoMesJ = 0.05 * rendimentoTotalJ
    rendimentoTotalJ += rendimentoMesJ
    meses += 1

print(f"Rendimento Carlos = {rendimentoTotalC:.2f}")
print(f"Rendimento João = {rendimentoTotalJ:.2f}")
print(f"Qtd meses = {meses}")