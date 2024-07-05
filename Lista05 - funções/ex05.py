def maior(a, b, c):
    maior = a
    if(b > maior):
        maior = b
    if(c > maior):
        maior = c
    return maior

print(maior(12, 5, 10))