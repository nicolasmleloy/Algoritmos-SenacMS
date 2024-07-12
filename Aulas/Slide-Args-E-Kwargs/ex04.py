def consumo(p, t):
    consumo = (p * t) / 1000
    return consumo

resConsumo = consumo(300, 8)

def contaDeEnergia(resConsumo, valorKwh):
    conta = resConsumo * valorKwh
    return conta

conta = contaDeEnergia(resConsumo, 28.84)
print(f"Conta de energia = R${conta}")