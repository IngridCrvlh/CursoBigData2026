#git add . : Adiciona todos os arquivos modificados e novos da pasta atual de uma só vez.
#git commit -m "Mensagem clara do que foi feito": Salva um "retrato" das alterações

# nome = input("Informe o seu nome:")

# if nome=="Pyetro":
#     resposta="Pyetro presente!"
# elif nome=="Phellipe"
#      resposta= "Phellipe presente!"

mes= int(input("Infome o mês de nascimento:"))
#VISÃO ELIF
# if mes==1:
#     signo="Aquario" 
# elif mes==2:
#     signo="Peixes"
# elif mes==3:
#     signo="Áries"
# elif mes==4:
#     signo="Touro"
# elif mes==5:
#     signo="Gêmeos"
# elif mes==6:
#     signo="Câncer"
# elif mes==7:
#     signo="Leão"
# elif mes==8:
#     signo="Virgem"
# elif mes==9:
#     signo="Libra"
# elif mes==10:
#     signo="Escorpião"
# elif mes==11:
#     signo="Sagitário"
# elif mes==12:
#     signo="Capricórnio"

# print(f"Seu signo é {signo}:")

#VISÃO MATCH CASE

match mes:
    case 1:
        signo="Aquário"
    case 2:
        signo="Áries"
    case 3:
        signo="Touro"
    case 4:
        signo="Gêmeos"
    case 5:
        signo="Câncer"
    case _:
        signo="Número de mês inválido"

print(f"{signo}.") 
