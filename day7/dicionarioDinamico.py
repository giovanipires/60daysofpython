aluno = {}

aluno["Nome"] = input("Digite o nome do aluno: ")
aluno["Idade"] = int(input("Digite a idade do aluno: "))
aluno["Curso"] = input("Digite o curso do aluno: ")
aluno["Matrícula"] = int(input("Digite o nome do aluno: "))

for key, values in aluno.items():
    print(key, values)