def consumo(km, litros):
    consumo = km/litros
    
    if(consumo < 8):
        return "Gasta muito!"
    elif(consumo >= 8 and consumo <= 15):
        return "Econômico!"
    elif(consumo > 15):
        return "Super econômico!"
    
print(consumo(500, 40))