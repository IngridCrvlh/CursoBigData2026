#1. Cálculo de Lâmpadas:
#1 potênia da lâmpada, em watts
#2 largura do cômodo, em metros
#3 comprimento do cômodo, em metros

#regras
# para cada 1 m2 são necessárias 3 watts
# para cada 3m2 existe uma lâmpada


largura = 4
comprimento = 5
area = largura * comprimento

#4x5 = 20m2
#são necessárias 3 watts por m2
#20x3=60

potencia_neessaria = area * 3

#a cada 3m2 existe um bucal para 1 lâmpada
#20/3= 6,66


quantidade_de_lampadas = int(area / 3)

#valores de largura/comprimento/potencia
#input () = recebe o que a pessoa digitar
#float () = transforma aquilo em número decimal

import math
largura = float(input ("Digite a largura do cômodo: "))
comprimento =  float(input("Digite o comprimento do cômodo: "))
potencia_lampada = float(input("Digite a potência da lâmpada em watts: "))

area = largura * comprimento
potencia_nessaria = area * 3
quantidade_de_lampadas = int(area / 3)
print("Área do cômodo", area, "m2")
print("Potência necessária:", potencia_nessaria, "watts")
print("Quantidade de lâmpadas:", quantidade_de_lampadas)

quantidade_por_potencia = int(potencia_nessaria / potencia_lampada)
