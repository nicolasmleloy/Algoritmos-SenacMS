print("Lojas de dois - Tabela de preços\n")

def tabela():
    preco = 1.99
    for i in range(1, 51):
        print(f"{i} - R$ {preco:.2f}")
        preco += 1.99

tabela()