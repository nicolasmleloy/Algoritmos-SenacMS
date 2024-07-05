valorVenda = float(input("Informe o valor da venda: "))

if(valorVenda >= 100000):
    comissao = 700 + (0.16 * valorVenda)
    print(f"Comissão = {comissao} reais")
elif(valorVenda < 100000) and (valorVenda >= 80000):
    comissao = 650 + (0.14 * valorVenda)
    print(f"Comissão = {comissao} reais")
elif(valorVenda < 80000) and (valorVenda >= 60000):
    comissao = 600 + (0.14 * valorVenda)
    print(f"Comissão = {comissao} reais")
elif(valorVenda < 60000) and (valorVenda >= 40000):
    comissao = 500 + (0.14 * valorVenda)
    print(f"Comissão = {comissao} reais")
elif(valorVenda < 40000) and (valorVenda >= 20000):
    comissao = 500 + (0.14 * valorVenda)
    print(f"Comissão = {comissao} reais")
elif(valorVenda < 20000):
    comissao = 400 + (0.14 * valorVenda)
    print(f"Comissão = {comissao} reais")