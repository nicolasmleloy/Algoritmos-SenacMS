custoFabrica = float(input("Informe o custo de fábrica: "))

if(custoFabrica < 12000):
    distribuidor = 0.05 * custoFabrica
    print(f"Custo ao consumidor = {custoFabrica + distribuidor}")
elif(custoFabrica >= 12000) and (custoFabrica <= 25000):
    distribuidor = 0.10 * custoFabrica
    imposto = 0.15 * custoFabrica
    print(f"Custo ao consumidor = {custoFabrica + distribuidor + imposto}")
elif(custoFabrica > 25000):
    distribuidor = 0.15 * custoFabrica
    imposto = 0.20 * custoFabrica
    print(f"Custo ao consumidor = {custoFabrica + distribuidor + imposto}")