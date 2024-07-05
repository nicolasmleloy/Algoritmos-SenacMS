def calculo():
    qtd = int(input("Infrome a qtd de peixe: "))
    if(qtd > 50):
        excesso = 0
        multa = 4.00
        for i in range(50, qtd):
            multa += 4.00
            excesso += 1
        print(f"{excesso} kg além do limite! Multa = {multa}")
    else:
        print("Nenhum excesso. Tudo certo!")

calculo()