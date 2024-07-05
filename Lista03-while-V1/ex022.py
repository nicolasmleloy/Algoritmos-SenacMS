print("A) Para calcular média")
print("Qualquer outra tecla para ENCERRAR")
opcao = input("Escolha uma opção: ")
i = 1
soma = 0

while(opcao == "A"):
    nota = float(input("Infome sua nota: "))
    if(nota >= 0) and (nota <= 10):
        soma += nota
        print(f"Média = {soma / i}")
    else:
        print("Valor de nota inválido!")
    i += 1
    
    print("A) Para calcular média")
    print("B) Para encerrar programa")
    opcao = input("Escolha uma opção: ")