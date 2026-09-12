# # Aula 01: Logica de Programação
# # Preparando ambiente dev

# print("Olá mundo") # comando para imprimir

# # declarando uma variavel
# idade = 30 #número inteiro =INT
# nome = 'Maria' #texto =STRING
# preco = 19.99 #decimal - FLOAT

# print (idade)

#algoritimo BOLETIM:

#Desafio 1: Ordenação de Três Números

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Determinar ordem
if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(f"{num1}, {num2}, {num3}")
    else:
        print(f"{num1}, {num3}, {num2}")
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print(f"{num2}, {num1}, {num3}")
    else:
        print(f"{num2}, {num3}, {num1}")
else:
    if num1 <= num2:
        print(f"{num3}, {num1}, {num2}")
    else:
        print(f"{num3}, {num2}, {num1}")

#Desafio 2: Cálculo de Média e Status do Estudante
nota1 = 2
nota2 = 4

media = (nota1 + nota2)/2
print("A média final do estudante é" ,media, ".") 

#Atividade da Calculadora
numero1 = 50
numero2 = 35
soma = (numero1 + numero2)
multiplicacao = (numero1 * numero2)
divisao = (numero1 / numero2)
subtracao = (numero1 - numero2)
print("O resultado da soma é:", soma,".")
print("O resultado da multiplicação é:" ,multiplicacao,".")
print("O resultado da divisão é:" ,divisao,".")
print("O resultado da subtração é:" ,subtracao,".")