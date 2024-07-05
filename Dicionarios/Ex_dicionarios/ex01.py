lista = []

for empresas in range(4):
    nome = input("\nInforme o nome da empresa: ")
    unidade = input("Infrome a unidade: ")
    fone = input("Informe o fone: ")
    email = input("Informe o E-mail: ")
    cidade = input("Informe a cidade: ")
    uf = input("Informe a UF: ")

    empresa = {
        "Nome": nome,
        "Unidade": unidade,
        "Fone": fone,
        "E-mail": email,
        "Cidade": cidade,
        "UF": uf
    }

    lista.append(empresa)

    empresa["Nome"] = nome
    empresa["Unidade"] = unidade
    empresa["Fone"] = fone
    empresa["E-mail"] = email
    empresa["Cidade"] = cidade
    empresa["UF"] = uf

for i in lista:
    print(i)