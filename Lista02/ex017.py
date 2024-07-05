salario = float(input("Infome o salário: "))
valorPrest = float(input("Informe o valor da prestação: "))

if(valorPrest > (0.20 * salario)):
    print("Empréstimo não concedido!")
else:
    print("Empréstimo concedido!")