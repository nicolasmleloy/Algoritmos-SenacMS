def operacoes(a, b, simbolo):
    if(simbolo == "+"):
        operacao = a + b
    elif(simbolo == "-"):
        operacao = a - b
    elif(simbolo == "/"):
        operacao = a / b
    elif(simbolo == "*"):
        operacao = a * b
    else:
        print("Símbolo inválido!")
        
    return operacao

print(operacoes(2, 4, "+"))