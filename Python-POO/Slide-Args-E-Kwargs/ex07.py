def desconto(dia, **kwargs):
    conta = kwargs["valor"]
    print(f"Conta S/ taxas: {conta}")
    print("Conta C/ taxas:")
    taxa = (conta * kwargs["taxa"])
    couvert = kwargs["couvert"]
    total = conta + taxa + couvert
    if(dia == "terca-feira"):
        print(f" Rodízio: {conta:.2f}")
        print(f" Taxa de serviço: {taxa:.2f}")
        print(f" Couvert: {couvert:.2f}")
        desconto = total * 0.10
        print(f" TOTAL COM DESCONTO = {total - desconto:.2f}")
    elif(dia == "quarta-feira"):
        print(f" Rodízio: {conta:.2f}")
        print(f" Taxa de serviço: {taxa:.2f}")
        print(f" Couvert: {couvert:.2f}")
        desconto = total * 0.15
        print(f" TOTAL COM DESCONTO = {total - desconto:.2f}")
    elif(dia == "quinta-feira"):
        print(f" Rodízio: {conta:.2f}")
        print(f" Taxa de serviço: {taxa:.2f}")
        print(f" Couvert: {couvert:.2f}")
        desconto = total * 0.20
        print(f" TOTAL COM DESCONTO = R${total - desconto:.2f}")

desconto("quarta-feira", valor = 79.92, taxa = 0.10, couvert = 15)
