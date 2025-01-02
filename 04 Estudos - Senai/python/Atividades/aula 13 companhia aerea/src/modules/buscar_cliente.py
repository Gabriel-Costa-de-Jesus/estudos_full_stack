from src.shared_data import lista_clientes

def buscar_cliente():
    procurar_cliente = input("Digite o nome do cliente para procurar: ")

    cliente_encontrado = None

    # Localizando o cliente na lista
    for cliente in lista_clientes:
        if procurar_cliente.lower() == cliente.cliente_reserva.lower():
            cliente_encontrado = cliente
            break

    # Se o cliente foi encontrado, remove-o e ajusta o número de assentos
    if cliente_encontrado:
        print(f"Cliente {cliente_encontrado.cliente_reserva} Encontrado do Sistema!")
    else:
        print("Pessoa não encontrada no sistema! Verifique se você digitou corretamente.")