m2 = float(input("Informe a área a ser pintada em metros quadrados: "))
areaLata = 108
areaGalao = 21.6

qtdLatas = m2 / areaLata
qtdGalao = m2 / areaGalao

print(f"[SOMENTE LATAS DE 18 LITROS]: Quantidade de tintas = {qtdLatas * 18}. Valor total = {qtdLatas * 80}")
print(f"[SOMENTE LATAS DE 3,6 LITROS]: Quantidade de tintas = {qtdLatas * 3.6}. Valor total = {qtdLatas * 25}")a