#3 Tentativa de Login e Senha

usuario_correto = "admin"
senha_correta = "123456"

tentativas = 3

while tentativas > 0:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado com sucesso!")
        break
    else:
        tentativas = tentativas - 1
        print("Usuário ou senha incorretos.")
        print("Tentativas restantes:", tentativas)

if tentativas == 0:
    print("Acesso bloqueado!")