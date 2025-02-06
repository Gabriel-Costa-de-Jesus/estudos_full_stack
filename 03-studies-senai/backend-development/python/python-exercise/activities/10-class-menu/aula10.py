def adicionar_item():
    print("--" * 30)
    item = input("Digite o nome do item para adicionar ao cardápio: ")
    preco = input("Digite o valor do item: ")
    preco = preco.replace("R$", "").replace(" ", "").replace(",", ".")
    preco = float(preco)
    cardapio[item] = preco

    # Formata o preço com duas casas decimais e troca o ponto por vírgula
    preco_formatado = f"{preco:.2f}".replace(".", ",")

    print(f"{item} R${preco_formatado} Adicionado com Sucesso!")
    print("--" * 30)


def remover_item():
    if not cardapio: # Se tiver vazio faça
       print("--"*30)
       print("Adicione um item primeiro para depois ser removido!")
       print("--"*30)
    else:
         print("--"*30)
         remove_item = input("Digite o nome do item para ser removido")
         if remove_item in cardapio:
            cardapio.pop(remove_item)
            print(f"O item {remove_item} foi removido com sucesso")
            print(cardapio)
            print("--"*30)

def registrar_pedido():
    print(cardapio)
    opcao_cliente = input("Escolha a sua opção: ")
    if opcao_cliente in cardapio:
        lista_pedidos.append(opcao_cliente)
        pedidos[opcao_cliente] = numero_do_pedido
        print(f"Total dos pedidos: {len(lista_pedidos)}")
        
def calcular_total_pedido():
    global total  # Declara que estamos usando a variável global 'total'
    total = 0  # Reseta o total para evitar somas duplicadas
    
    for itens_pedidos in lista_pedidos:  # Percorre os itens registrados na lista de pedidos
        if itens_pedidos in cardapio:
            total += cardapio[itens_pedidos]  # Soma o valor correspondente no cardápio
    
    # Formata o total com duas casas decimais e troca o ponto por vírgula
    total_formatado = f"{total:.2f}".replace(".", ",")
    print(f"O Valor total dos pedidos é R${total_formatado}")
    return total_formatado

def exibir_pedidos():           
    print("Pedidos feitos até o momento \n", pedidos)
    print(f"Total de todos os pedidos: {total_formatado}")
    

def exibir_menu():
    print("--"*30)
    print("O que você deseja fazer?")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Registrar pedido")
    print("4 - Calcular total do pedido")
    print("5 - Exibir todos os pedidos")
    print("6 - Sair do programa")
    opcao_menu = int(input("Escolha a sua opção: "))
    print("--"*30)
    return opcao_menu

def sair():
    print("Saindo do Sistema")

def erro():
    print("Opção Inválida! Tente Novamente!")
    
cardapio = {}
pedidos = {}
lista_pedidos = []
numero_do_pedido = 0
total = 0

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
        total_formatado = calcular_total_pedido()
        exibir_pedidos()
    elif opcao_menu == 6:
        sair()
        break
    else:
        erro()

