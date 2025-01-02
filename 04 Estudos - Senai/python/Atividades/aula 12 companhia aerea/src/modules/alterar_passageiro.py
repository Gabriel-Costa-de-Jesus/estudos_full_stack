from src.models import Class_reserva
from src.shared_data import lista_aviao, lista_clientes
def alterar_passageiro():

    print("Clientes Cadastrados no Sistema")

    # Exibindo as reservas cadastradas
    for reservas in lista_clientes:
        print(f"Número do Avião: Nº {reservas.aviao_reserva_numero}\n"
              f"Nome do Avião: {reservas.aviao_reserva_nome}\n"
              f"Cliente: {reservas.cliente_reserva}\n"
              f"Número do Assento: Nº {reservas.assento_reserva}\n")

    # Solicitando o nome do cliente para alterar a reserva
    alterar_reserva = input("Digite o nome do cliente para alterar a reserva: ")

    cliente_encontrado = None

    # Localizando o cliente na lista
    for cliente in lista_clientes:
        if alterar_reserva.lower() == cliente.cliente_reserva.lower():
            cliente_encontrado = cliente
            break

    # Se o cliente foi encontrado, remove-o e ajusta o número de assentos
    if cliente_encontrado:
        print(f"Cliente {cliente_encontrado.cliente_reserva} Encontrado do Sistema!")

        # Aqui ajustamos o número de assentos no avião correspondente
        for aviao in lista_aviao:
            if aviao.numeracao_do_aviao == cliente_encontrado.aviao_reserva_numero:
                aviao.assentos_do_aviao += 1
                break

        # Removendo o cliente da lista
        lista_clientes.remove(cliente_encontrado)
    else:
        print("Pessoa não encontrada no sistema! Verifique se você digitou corretamente.")


    # Exibe os aviões disponíveis
    print("Aviões disponíveis:")
    for aviao in lista_aviao:
        print(aviao.nome_do_aviao) # Nesse momento aviao se tornar uma instancia pois recebe um dado da lista_aviao

    escolha_aviao = input("Digite o Número do Avião correspondente ou o nome para o cliente ser Alterado: ")
    
    # Verifica se o avião escolhido está na lista
    aviao_encontrado = None
    for aviao in lista_aviao:
    # Convertendo escolha_aviao para int, se possível
        if escolha_aviao.isdigit() and int(escolha_aviao) == aviao.numeracao_do_aviao:  # Comparação por número
            aviao_encontrado = aviao # o isdigit serve para verificar se a pessoa digitou um número válido, se sim, é convertido para int já que escolha aviao é str, após isso essa linha é executada
            break
        elif escolha_aviao.lower() == aviao.nome_do_aviao.lower():  # Comparação por nome
            aviao_encontrado = aviao # Nesse momento do código avião_encontrado passa a se tornar uma instancia do meu código que se consegue conectar a Class
            break 
    
    if aviao_encontrado: # No python, se a variável tiver algum valor ela é True, e a condição é executada
        print(f"Avião {aviao_encontrado.nome_do_aviao} encontrado!")
        
        # Verifica se há assentos disponíveis
        if aviao_encontrado.assentos_do_aviao > 0:
            aviao_encontrado.assentos_do_aviao -= 1  # Atualiza o número de assentos disponíveis
            numero_assento = aviao_encontrado.assentos_do_aviao + 1
            print(f"Seu assento é o número {numero_assento}")

             # Cria uma nova instância de reserva
            nova_reserva = Class_reserva(
                aviao_reserva_numero=aviao_encontrado.numeracao_do_aviao, #aviao_encontrado pertence a class aviao, ele é uma referencia para a class aviao
                aviao_reserva_nome=aviao_encontrado.nome_do_aviao,
                cliente_reserva=alterar_reserva,
                assento_reserva=numero_assento
            )

            # Adiciona a reserva na lista de clientes
            lista_clientes.append(nova_reserva)
        else: # O aviao encontrado ele consegue se conectar a Class porque ele recebe os dados(objeto) correspondente a um dado presente da CLass
            print("Desculpe, não há mais assentos disponíveis.")
    else:
        print("Avião não encontrado no sistema.")