matriz = []

for linha in range(5):
    l = []
    for coluna in range(5): 
        if(linha == coluna):
            l.append(1)
        else:
            l.append(0)
    print(l)
