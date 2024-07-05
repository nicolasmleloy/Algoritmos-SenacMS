alunos = [("João", 3.0), ("Maria", 9.5), ("Pedro", 7.5), ("Ana", 8.5)]
maior = alunos[0]

for aluno in alunos:
    if(aluno[1] > maior[1]):
        maior = aluno
    
print(maior)