def adicionar_item():
    print("--" * 30)
    item = input("Digite o nome do item para adicionar ao cardápio: ")
    preco = input("Digite o valor do item: ")
    preco = preco.replace("R$", "").replace(" ", "").replace(",", ".")
    preco = float(preco)
    cardapio[item] = preco

    # Formata o preço com duas casas decimais e troca o ponto por vírgula
    preco_formatado = f"{preco:.2f}".replace(".", ",")

    print(f"{item} R${preco_formatado} adicionado com sucesso!")
    print("--" * 30)


def remover_item():
    print("--" * 30)
    if not cardapio:
        print("O cardápio está vazio. Adicione um item primeiro!")
    else:
        remove_item = input("Digite o nome do item para ser removido: ")
        if remove_item in cardapio:
            cardapio.pop(remove_item)
            print(f"O item {remove_item} foi removido com sucesso.")
        else:
            print(f"O item '{remove_item}' não está no cardápio.")
    print("--" * 30)


def registrar_pedido():
    print("--" * 30)
    print("Itens disponíveis no cardápio:")
    for item, preco in cardapio.items():
        preco_formatado = f"{preco:.2f}".replace(".", ",")
        print(f"{item} - R${preco_formatado}")
    print("--" * 30)

    opcao_cliente = input("Digite o nome do item que deseja pedir: ")
    if opcao_cliente in cardapio:
        lista_pedidos.append(opcao_cliente)
        pedidos[opcao_cliente] = numero_do_pedido
        print(f"{opcao_cliente} adicionado ao pedido com sucesso!")
    else:
        print("Item não encontrado no cardápio.")
    print("--" * 30)


def calcular_total_pedido():
    print("--" * 30)
    global total
    total = 0

    for item_pedido in lista_pedidos:
        if item_pedido in cardapio:
            total += cardapio[item_pedido]

    total_formatado = f"{total:.2f}".replace(".", ",")
    print(f"O valor total dos pedidos é: R${total_formatado}")
    print("--" * 30)
    return total_formatado


def exibir_pedidos():
    print("--" * 30)
    if not lista_pedidos:
        print("Nenhum pedido registrado até o momento.")
    else:
        print("Pedidos feitos até o momento:")
        for item in lista_pedidos:
            print(f"- {item}")
        print(f"Total acumulado: R${calcular_total_pedido()}")
    print("--" * 30)


def exibir_menu():
    print("--" * 30)
    print("O que você deseja fazer?")
    print("1 - Adicionar item ao cardápio")
    print("2 - Remover item do cardápio")
    print("3 - Registrar pedido")
    print("4 - Calcular total do pedido")
    print("5 - Exibir todos os pedidos")
    print("6 - Sair do programa")
    opcao_menu = int(input("Escolha a sua opção: "))
    print("--" * 30)
    return opcao_menu


def sair():
    print("--" * 30)
    print("Saindo do sistema...")
    print("--" * 30)


def erro():
    print("--" * 30)
    print("Opção inválida! Tente novamente.")
    print("--" * 30)


# Variáveis globais
cardapio = {}
pedidos = {}
lista_pedidos = []
numero_do_pedido = 0
total = 0

# Loop principal
while True:
    opcao_menu = exibir_menu()

    if opcao_menu == 1:
        adicionar_item()
    elif opcao_menu == 2:
        remover_item()
    elif opcao_menu == 3:
        numero_do_pedido += 1
        registrar_pedido()
    elif opcao_menu == 4:
        calcular_total_pedido()
    elif opcao_menu == 5:
        exibir_pedidos()
    elif opcao_menu == 6:
        sair()
        break
    else:
        erro()
