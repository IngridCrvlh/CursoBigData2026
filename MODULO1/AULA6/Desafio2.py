#2. Cadastro Seletivo de Candidatos

candidatos_validos = []

for i in range(5):
    print(f"\nCandidato {i + 1}")

    nome = input("Nome: ")
    idade = int(input("Idade: "))

    if idade < 18:
        print("Candidato rejeitado: menor de 18 anos.")
    else:
        email = input("E-mail: ")

        candidato = {
            'nome': nome,
            'idade': idade,
            'email': email
        }

        candidatos_validos.append(candidato)

print("\n" + "-" * 40)
print("CANDIDATOS VÁLIDOS")
print("-" * 40)

for candidato in candidatos_validos:
    print(f"Nome: {candidato['nome']}")
    print(f"Idade: {candidato['idade']}")
    print(f"E-mail: {candidato['email']}")
    print("-" * 40)