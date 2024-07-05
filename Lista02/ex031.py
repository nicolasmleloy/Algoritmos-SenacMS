dist = float(input("Informe a distância percorrida: "))
l = float(input("Informe a quantidade de litros de gasolina consumidos: "))

consumo = dist / l

if(consumo < 8):
    print("venda o carro!")
elif(consumo >= 8) and (consumo <= 14):
    print("Econômico!")
elif(consumo > 12):
    print("Super econômico!")