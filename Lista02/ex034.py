preco = int(input("Informe um preço: "))

if(preco <= 50):
    aumento = preco * 0.05
    print(f"Novo preço = {preco + aumento}")
elif(preco > 50) and (preco <= 100):
    aumento = preco * 0.10
    print(f"Novo preço = {preco + aumento}")
elif(preco > 100):
    aumento = preco * 0.15
    print(f"Novo preço = {preco + aumento}")