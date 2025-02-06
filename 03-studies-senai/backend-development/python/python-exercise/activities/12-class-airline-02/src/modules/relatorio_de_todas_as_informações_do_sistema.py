from src.shared_data import lista_aviao, lista_clientes, reservas_do_aviao

def relatorio_de_todas_as_informações_do_sistema():
    if not lista_aviao:
        print("Nenhum avião cadastrado no sistema.")
        return

    print("Relatório de Informações do Sistema")
    print("-" * 40)

    for aviao in lista_aviao: # referencia aviao para se conectar a class e lista aviao e pegar os dados
        for reserva in lista_clientes: # referencia reserva para se conectar a class e a lista de clientes
            if reserva.aviao_reserva_numero == aviao.numeracao_do_aviao: #
                reservas_do_aviao.append(reserva)

        total_assentos = aviao.assentos_do_aviao + len(reservas_do_aviao)
        assentos_ocupados = len(reservas_do_aviao)
        assentos_disponiveis = total_assentos - assentos_ocupados

        # Exibição das informações
        print(f"Número do Avião: Nº {aviao.numeracao_do_aviao}")
        print(f"Nome do Avião: {aviao.nome_do_aviao}")
        print(f"Total de Assentos: {total_assentos}")
        print(f"Assentos Ocupados: {assentos_ocupados}")
        print(f"Assentos Disponíveis: {assentos_disponiveis}")
        print("-" * 40)
