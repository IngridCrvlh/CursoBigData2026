#3. Rendimento do Taxista:
odometro_inicial = int(input("Digite a marcação inicial do odômetro: "))
odometro_final = int(input("Digite a marcação final do odômetro: "))
litros = int(input("Digite a quantidade de litros de combustível gastos: "))
valor_passageiros = int(input("Digite o valor recebido dos passageiros: "))

quilometros = odometro_final - odometro_inicial

consumo = quilometros / litros

custo_combustivel = litros * 6.15

lucro = valor_passageiros - custo_combustivel

print("Quilômetros percorridos:", quilometros, "km")
print("Consumo médio:", consumo, "km/L")
print("Lucro líquido: R$", lucro)