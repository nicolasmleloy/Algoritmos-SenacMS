def calculoSalario(qtdHoras, valorHora):
    salario = qtdHoras * valorHora
    if(qtdHoras > 40):
        i = 40
        while(i < qtdHoras):
            salario += valorHora / 2
            i += 1
    print(f"Salário = {salario:.3f}")

calculoSalario(45, 20)