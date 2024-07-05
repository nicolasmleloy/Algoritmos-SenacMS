print("--" * 30)
print("Especificação     || Código || Preço")
print("Hot Dog           || 100    || 12.00")
print("X-Salada          || 102    || 18.50")
print("X-Bacon           || 103    || 25.50")
print("X-Burguer         || 104    || 17.00")
print("Suco de laranja   || 105    || 9.50")
print("Refrigerante      || 106    || 6.00")
print("--" * 30)

codigo = int(input("Informe o código do produto: "))
qtd = int(input("Informe a quantidade desse produto: "))

if(codigo == 100):
    total = qtd * 12
    print(f"Total a pagar = {total}")
elif(codigo == 102):
    total = qtd * 18.50
    print(f"Total a pagar = {total}")
elif(codigo == 103):
    total = qtd * 25.50
    print(f"Total a pagar = {total}")
elif(codigo == 104):
    total = qtd * 17
    print(f"Total a pagar = {total}")
elif(codigo == 105):
    total = qtd * 9.50
    print(f"Total a pagar = {total}")
elif(codigo == 106):
    total = qtd * 6
    print(f"Total a pagar = {total}")
else:
    print(f"O código {codigo} não existe!")