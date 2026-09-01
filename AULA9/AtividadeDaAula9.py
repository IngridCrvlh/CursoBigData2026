def calcular_imc(peso, altura):
    imc= peso / (altura * altura)
    return imc

def obter_classificacao(imc):
    if imc < 18.5:
        resultado = "Abaixo do peso 😟"
    elif imc <25:
        resultado = "Peso normal 😁👌🏼"
    elif imc <30:
        resultado = "Sobre peso 😐"
    else: 
        resultado = "Obesidade 😨👎🏼"
        return resultado

quantidade = int(input("Quantas pessoas? "))
for i in range(quantidade): 
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    imc =  calcular_imc(peso, altura)
    classificacao = obter_classificacao(imc)

    print("IMC" , imc)
    print ("Classificação: ", classificacao)
