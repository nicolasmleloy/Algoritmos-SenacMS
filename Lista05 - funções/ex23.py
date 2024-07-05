import random

def sorteiaAluno(qtd):
    alunos = []
    for aluno in range(qtd):
        aluno = input("Digite um nome: ")
        alunos.append(aluno)
    
    sorteado = random.choice(alunos)
    return sorteado

print(f"O primeiro aluno(a) a apresentar será: {sorteiaAluno(5)}")