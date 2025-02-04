from src.shared_data import lista_aviao, lista_clientes

def cancelar_reserva():
    print("Clientes Cadastrados no Sistema")

    # Exibindo as reservas cadastradas
    for reservas in lista_clientes:
        print(f"Número do Avião: Nº {reservas.aviao_reserva_numero}\n"
              f"Nome do Avião: {reservas.aviao_reserva_nome}\n"
              f"Cliente: {reservas.cliente_reserva}\n"
              f"Número do Assento: Nº {reservas.assento_reserva}\n")

    # Solicitando o nome do cliente para cancelar a reserva
    cancela_reserva = input("Digite o nome do cliente para cancelar a reserva: ")

    cliente_encontrado = None

    # Localizando o cliente na lista
    for cliente in lista_clientes:
        if cancela_reserva.lower() == cliente.cliente_reserva.lower():
            cliente_encontrado = cliente
            break

    # Se o cliente foi encontrado, remove-o e ajusta o número de assentos
    if cliente_encontrado:
        print(f"Cliente {cliente_encontrado.cliente_reserva} Removido do Sistema!")

        # Aqui ajustamos o número de assentos no avião correspondente
        for aviao in lista_aviao:
            if aviao.numeracao_do_aviao == cliente_encontrado.aviao_reserva_numero:
                aviao.assentos_do_aviao += 1
                break

        # Removendo o cliente da lista
        lista_clientes.remove(cliente_encontrado)
    else:
        print("Pessoa não encontrada no sistema! Verifique se você digitou corretamente.")
