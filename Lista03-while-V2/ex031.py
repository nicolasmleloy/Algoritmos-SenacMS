salario = (4000 * (1.5 / 100)) + 4000
anoAtual = int(input("Informe o ano atual: "))

for i in range(2021, anoAtual):
    salario *= 2
    print(i)

print(f"Salário atual = {salario}")