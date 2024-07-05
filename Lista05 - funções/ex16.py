import random

def embaralhar(palavra: str):
    letras = list(palavra)
    palavraEmbaralhada = random.sample(letras, len(letras))
    for i in range(len(letras)):
        print(palavraEmbaralhada[i], end="")

embaralhar("hello")