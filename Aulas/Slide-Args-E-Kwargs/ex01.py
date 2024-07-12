def frutas(*frutas):
    v = 1
    for f in frutas:
        print(f"{v}, {f}")
        v += 1

frutas("Pera", "Uva", "Maçã", "Salada mista")