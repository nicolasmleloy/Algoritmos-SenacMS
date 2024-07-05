def calcularTempo(tempo):
    valorHora = 9.00
    valorHoraAdicional = 1.50
    pis = 3.3 / 100
    cofins = 2.0 / 100
    icms = 17.0 / 100

    horas = tempo / 60.0
    print(f"Tempo: {horas:.1f} horas")

    if (tempo < 15):
        total = 0.0
        print("\nTempo utilizado NÃO cobrado!\n")
    else:
        if (horas <= 1):
            total = valorHora
        else:
            horas_extras = horas - 1
            total = valorHora + (horas_extras * valorHoraAdicional)
        
        pis_valor = pis * total
        cofins_valor = cofins * total
        icms_valor = icms * total
        impostos = pis_valor + cofins_valor + icms_valor

        print(f"PIS: R$ {pis_valor:.2f}")
        print(f"COFINS: R$ {cofins_valor:.2f}")
        print(f"ICMS: R$ {icms_valor:.2f}")
        print(f"IMPOSTOS: R$ {impostos:.2f}")
        print(f"TOTAL: R$ {total:.2f}")

# Exemplo de uso
tempo = int(input("Informe o tempo utilizado em MINUTOS: "))
calcularTempo(tempo)