import random
p1 = str(input("Digite o primeiro aluno: "))
p2 = str(input("Digite o segundo aluno: "))
p3 = str(input("Digite o terceiro aluno: "))
p4 = str(input("Digite o quarto aluno: "))
alunos = [p1,p2,p3,p4]
random.shuffle(alunos)
print("A ordem de apresentação será:")
print(alunos)