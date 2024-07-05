soma = 0
i = 0

while(True):
    idade = int(input("Informe uma idade: "))
    if(idade != 0):
        soma += idade
    else:
        break
    i += 1

print(f"Média de idades = {soma / i}")