#1. Cálculo de Média Escolar para 10 Alunos

for aluno in range(1, 11):
    print("Aluno", aluno)

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    print("Média:", media)

    if media >= 6:
        print("Aprovado")
    elif media >= 3:
        print("Recuperação")
    else:
        print("Reprovado")

    print("--------------------")