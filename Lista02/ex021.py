notaTrabLab = float(input("Informe a nota do trabalho de laboratório: "))
avalSemest = float(input("Informe a nota da avaliação semestral: "))
exameFinal  = float(input("Informe a nota do exame final: "))

notaTrabLab *= 2
avalSemest *= 3
exameFinal *= 5

media = (notaTrabLab + avalSemest + exameFinal) / 10

if(media >= 0) and (media <= 2.9):
    print(f"Média = {media}")
    print("Reprovado!")
elif(media >= 3) and (media <= 5.9):
    print(f"Média = {media}")
    print("Recuperação!")
else:
    print(f"Média = {media}")
    print("Aprovado!")