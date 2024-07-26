nome = input("Informe seu nome: ")
senha = input("Informe uma senha: ")

def letraMaiuscula():
    for letra in letras: 
        if letra in senha:
            return True

letraMaiuscula = letraMaiuscula()

while(len(senha) < 8 and letraMaiuscula == True):
    if(len(senha) < 8 and letraMaiuscula == True):