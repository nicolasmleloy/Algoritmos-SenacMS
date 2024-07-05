valorAquisicao = float(input("Informe o valor de aquisição: "))

if(valorAquisicao < 50):
    aumento = 0.45 * valorAquisicao
    print(f"Valor de venda = {valorAquisicao + aumento}")
else:
    aumento = 0.30 * valorAquisicao
    print(f"Valor de venda = {valorAquisicao + aumento}")