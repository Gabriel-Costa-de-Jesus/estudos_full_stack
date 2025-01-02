from src.shared_data import lista_clientes

def reservas_cadastradas_no_sistema():
    print("Clientes Cadastrados no Sistema")

    for reservas in lista_clientes:
        print(f"Número do Avião: Nº {reservas.aviao_reserva_numero}\n"
              f"Nome do Avião: {reservas.aviao_reserva_nome}\n"
              f"Cliente: {reservas.cliente_reserva}\n"
              f"Número do Assento: Nº {reservas.assento_reserva + 1}\n")