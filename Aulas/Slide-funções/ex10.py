def financiamento():
    valorVeiculo = float(input("Infrome o valor do VEÍCULO: "))
    valorEntrada = float(input("Infrome o valor da ENTRADA: "))
    taxaJuros = float(input("Infrome a TAXA DE JUROS: "))
    qtdParcelas = int(input("Infrome a QTD DE PARCELAS: "))
    
    valorJuros = valorEntrada * (1 + taxaJuros/ 100) ** qtdParcelas
    valorTotal = valorVeiculo + valorJuros
    valorParcela = valorTotal / qtdParcelas

    print(f"Valor total pago = {valorTotal:.2f}")
    print(f"Quantia dos juros pagos = {valorJuros:.2f}")
    print(f"Valor de cada parcela = {valorParcela:.2f}")
    
financiamento()