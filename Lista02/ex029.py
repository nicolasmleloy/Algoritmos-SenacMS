idade = int(input("Informe a sua idade: "))
tempoServico = int(input("Informe o tempo de serviço: "))

if(idade >= 65) or (tempoServico >= 30) or (idade >= 60) and (tempoServico >= 25):
    print(f"Idade = {idade} e tempo de serviço = {tempoServico}. PODE APOSENTAR!")
else:
    print(f"Idade = {idade} e tempo de serviço = {tempoServico}. NÃO PODE APOSENTAR!")