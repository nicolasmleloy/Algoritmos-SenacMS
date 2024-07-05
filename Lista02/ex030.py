mg = 0.07
sp = 0.12
rj = 0.15
ms = 0.08

valor = float(input("Informe o valor do produto: "))
estado = input("Informe o estado de destino, mg, sp, rj ou ms: ")

if(estado == "mg"):
    imposto = valor * mg
    print(f"Valor com imposto = {valor + imposto}")
elif(estado == "sp"):
    imposto = valor * sp
    print(f"Valor com imposto = {valor + imposto}")
elif(estado == "rj"):
    imposto = valor * rj
    print(f"Valor com imposto = {valor + imposto}")
elif(estado == "ms"):
    imposto = valor * ms
    print(f"Valor com imposto = {valor + imposto}")
else:
    print("[ERRO]: Estado inválido!")