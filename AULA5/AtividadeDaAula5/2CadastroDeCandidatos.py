#2. Cadastro de Candidatos

for candidato in range(1, 13):
    print("Candidato", candidato)

    ano_nascimento = int(input("Digite o ano de nascimento: "))

    idade = 2026 - ano_nascimento

    if idade < 18:
        print("Você é menor de 18 anos e não pode participar.")
        print("--------------------")
        continue

    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    print("Candidato cadastrado com sucesso!")
    print("Telefone:", telefone)
    print("Email:", email)

    print("--------------------")