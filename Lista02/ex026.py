ano = int(input("Informe um ano: "))

if(ano % 4 == 0) or (ano % 400 == 0) and (ano % 100 != 0):
    print("Ano bissesto!")
else:
    print("Ano NÃO bissesto!")