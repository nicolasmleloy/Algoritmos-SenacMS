r1 = int(input("Informe o resistor R1: "))
r2 = int(input("Informe o resistor R2: "))

while(True):
    if(r1 == 0 or r2 == 0):
        break
    else:
        r = (r1 * r2) / (r1 + r2)
        print(f"R = {r:.2f}")

        r1 = int(input("Informe o resistor R1: "))
        r2 = int(input("Informe o resistor R2: "))