def data():
    try:
        data = input("Informe uma data: ")
        data = data.split("/")
        
        if(data[1] == "01"):
            print(f"{data[0]} de janeiro de {data[2]}")
        elif(data[1] == "02"):
            print(f"{data[0]} de fevereiro de {data[2]}")
        elif(data[1] == "03"):
            print(f"{data[0]} de março de {data[2]}")
        elif(data[1] == "04"):
            print(f"{data[0]} de abril de {data[2]}")
        elif(data[1] == "05"):
            print(f"{data[0]} de maio de {data[2]}")
        elif(data[1] == "06"):
            print(f"{data[0]} de junho de {data[2]}")
        elif(data[1] == "07"):
            print(f"{data[0]} de julho de {data[2]}")
        elif(data[1] == "08"):
            print(f"{data[0]} de agosto de {data[2]}")
        elif(data[1] == "09"):
            print(f"{data[0]} de setembro de {data[2]}")
        elif(data[1] == "10"):
            print(f"{data[0]} de outubro de {data[2]}")
        elif(data[1] == "11"):
            print(f"{data[0]} de novembro de {data[2]}")
        elif(data[1] == "12"):
            print(f"{data[0]} de dezembro de {data[2]}")
    except:
        print("[ERRO]: Inválido!")

data()