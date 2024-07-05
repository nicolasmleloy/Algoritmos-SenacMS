def somaImposto(taxaImposto, custo):
    custo += (taxaImposto / 100) * custo
    return custo

print(f"Novo valor = {somaImposto(5, 50)}")