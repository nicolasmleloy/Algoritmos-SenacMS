def soma(*args):
    soma = 0
    for i in args:
        print(i)
        soma += i

print(soma(4, 5, 7, 8, 2))