def reverso(n: int):
    n = str(n)
    for i in reversed(n):
        print(i, end="")

reverso(567)