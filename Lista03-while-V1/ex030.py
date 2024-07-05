try:
    vInicial = int(input("Informe um intervalo inicial: "))
    vFinal = int(input("Informe um intervalo final: "))
    soma = 0

    for i in range(vInicial, vFinal):
        if(i % 2 == 1):
            soma += i

    print(f"Soma dos ímpares = {soma}")
except:
    print("Intervalo inválido!")