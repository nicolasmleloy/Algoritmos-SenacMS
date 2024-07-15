def listaPadrao(qtd, v):
    lista = []
    for i in range(qtd):
        lista.append(v)
    
    return lista

res = listaPadrao(5, "A")
print(res)