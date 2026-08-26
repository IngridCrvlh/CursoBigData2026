#2. Quantidade de Caixas de Azulejos: 
import math

comprimento = int(input("Digite o comprimento da cozinha: "))
largura = int(input("Digite a largura da cozinha: "))
altura = int(input("Digite a altura da cozinha: "))

area_paredes = 2 * (comprimento * altura) + 2 * (largura * altura)

caixas = math.ceil(area_paredes / 1.5)

print("Área total das paredes:", area_paredes, "m²")
print("Quantidade de caixas necessárias:", caixas)