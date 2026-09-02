import random

numeros_pedidos = []
pedidos = []


def gerar_numero_pedido():
    numero_pedido = random.randint(1000, 9999)

    while numero_pedido in numeros_pedidos:
        numero_pedido = random.randint(1000, 9999)

    numeros_pedidos.append(numero_pedido)

    return numero_pedido


def criar_pedido(numero_mesa, id_garcom):
    numero_pedido = gerar_numero_pedido()

    novo_pedido = {
        "numero_pedido": numero_pedido,
        "numero_mesa": numero_mesa,
        "id_garcom": id_garcom,
        "itens": [],
        "status": "Aberto"
    }

    pedidos.append(novo_pedido)

    print("Pedido criado com sucesso!✅")

    return novo_pedido
