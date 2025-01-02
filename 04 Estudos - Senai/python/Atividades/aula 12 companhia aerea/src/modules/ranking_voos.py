from src.shared_data import lista_aviao, lista_clientes, lista_rank

def gerar_ranking_voos():

    # Contar o número de reservas para cada avião
    for aviao in lista_aviao:
        contador_reservas = 0
        for reserva in lista_clientes:
            if reserva.aviao_reserva_nome == aviao.nome_do_aviao:
                contador_reservas += 1
        # Adicionar o avião e o número de reservas na lista de ranking
        lista_rank.append((aviao.nome_do_aviao, contador_reservas))

    # Ordenar a lista usando Bubble Sort
    n = len(lista_rank)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista_rank[j][1] < lista_rank[j + 1][1]:  # Ordenar em ordem decrescente
                lista_rank[j], lista_rank[j + 1] = lista_rank[j + 1], lista_rank[j]

    # Exibir o ranking
    print("\nRanking dos Aviões Mais Ocupados:")
    for i, (nome_aviao, reservas) in enumerate(lista_rank, start=1):
        print(f"{i}. {nome_aviao} - {reservas} reservas")
    
    return lista_rank
