from src.models import Class_reserva
from src.shared_data import lista_aviao, lista_clientes

def cadastrar_cliente():
    nome_do_cliente = input("Digite o nome do cliente para ser cadastrado:\n")

    # Exibe os aviões disponíveis
    print("Aviões disponíveis:")
    for aviao in lista_aviao:
        print(f"{aviao.numeracao_do_aviao} - {aviao.nome_do_aviao}")

    escolha_aviao = input("\nDigite o Número do Avião correspondente ou o nome para o cliente ser cadastrado:\n")
    
    # Verifica se o avião escolhido está na lista
    aviao_encontrado = None 
    for aviao in lista_aviao:
        # Convertendo escolha_aviao para int, se possível
        if escolha_aviao.isdigit() and int(escolha_aviao) == aviao.numeracao_do_aviao:  # o isdigit serve para verificar se a pessoa digitou um número válido, se sim, é convertido para int já que escolha aviao é str, após isso essa linha é executada
            aviao_encontrado = aviao
            break
        elif escolha_aviao.lower() == aviao.nome_do_aviao.lower():
            aviao_encontrado = aviao
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
                cliente_reserva=nome_do_cliente,
                assento_reserva=numero_assento
            ) 

            # Adiciona a reserva na lista de clientes
            lista_clientes.append(nova_reserva)
            print("Reserva cadastrada com sucesso!")
        else:
            print("Desculpe, não há mais assentos disponíveis.")
    else:
        print("Avião não encontrado no sistema.")
