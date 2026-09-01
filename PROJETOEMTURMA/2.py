Função criar_pedido()
# Lista que irá armazenar os pedidos
pedidos = []


def criar_pedido(numero_pedido, numero_mesa, id_garcom):
    pedido = {
        "numero_pedido": numero_pedido,
        "numero_mesa": numero_mesa,
        "id_garcom": id_garcom,
        "itens": [],
        "status": "Aberto"
    }

    pedidos.append(pedido)

    print("Pedido criado com sucesso!")
    print(f"Número do pedido: {numero_pedido}")
    print(f"Mesa: {numero_mesa}")
    print(f"Garçom: {id_garcom}")

    return pedido