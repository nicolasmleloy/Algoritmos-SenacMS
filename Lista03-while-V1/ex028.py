soma1 = 0
soma2 = 0
for i in range(1, 100):
    for c in range(1, 51):
        soma1 += i
        soma2 += c
        div = soma1 / soma2

print(f"S = {div}")