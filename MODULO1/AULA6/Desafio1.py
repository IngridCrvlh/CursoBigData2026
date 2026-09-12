#1. Média Escolar para 5 Estudantes

resultados = []

for i in range(5):
    print(f"\nAluno {i + 1}")

    nome = input("Nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    if media >= 7:
        resultado = "Aprovado"
    elif media >= 5:
        resultado = "Recuperação"
    else:
        resultado = "Reprovado"

    resultados.append(f"{nome} - Média: {media:.1f} - {resultado}")

print("\n" + "-" * 40)
print("RESULTADO FINAL")
print("-" * 40)

for resultado in resultados:
    print(resultado)