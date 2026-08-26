#5. Média do Aluno com Optativa

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
optativa = float(input("Digite a nota da optativa (-1 caso não tenha feito): "))

if optativa != -1:
    if nota1 < nota2:
        nota1 = optativa
    else:
        nota2 = optativa

media = (nota1 + nota2) / 2

print("Média:", media)

if media >= 6.0:
    print("Aprovado")
elif media >= 3.0:
    print("Recuperação")
else:
    print("Reprovado")