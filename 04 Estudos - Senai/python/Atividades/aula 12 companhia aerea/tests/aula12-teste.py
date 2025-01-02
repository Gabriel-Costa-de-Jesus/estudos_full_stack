def menu_aviao():
    print("--"*30)
    print("Escolha a opção desejada")
    print("1 - Cadastrar Avião")
    print("2 - Exibir Aviões Cadastrado nos Sistemas")
    print("3 - Cadastrar Cliente")
    print("4 - Cancelar reserva")
    print("5 - Reservas Cadastradas no Sistema")
    print("6 - Buscar cliente Cadastrado no Sistema")
    print("7 - Alterar Passageiro")
    print("8 - Relatório de todas as informações do Sistema")
    print("9 - Sair")
    opcao = int(input("Digite o número da sua Opção: "))
    print("--"*30)
    return opcao 

def cadastrar_aviao():
    global contador_aviao
    contador_aviao += 1
    nome_aviao = input("Digite o nome do avião para ser cadastrado: ")
    assentos_aviao = input("Digite a quantidade de assentos do avião: ")
    print(f"\nO avião Nº {contador_aviao}: {nome_aviao} com {assentos_aviao} assentos foi cadastrado com Sucesso!")
    info_aviao = Class_aviao(contador_aviao, nome_aviao, assentos_aviao)
    lista_aviao.append(info_aviao)

def exibir_informacoes():
    print("--"*30)
    for info_aviao in lista_aviao:
        print(f"Númeração do avião: {info_aviao.numeracao_do_aviao} \nNome do Avião: {info_aviao.nome_do_aviao} \nQuantidade de Assentos Disponíveis: {info_aviao.assentos_do_aviao} assentos \n")
    print("--"*30)

def cadastrar_cliente():
    nome_do_cliente = input("Digite o nome do cliente para ser cadastrado")
    escolha_aviao = input("Digite o Número do Avião correspondente ou o nome para o cliente ser Cadastrado")
    if escolha_aviao in lista_aviao:
        print("teste") # Consertar dps

def sair():
    print("Saindo do Sistema...")

class Class_aviao:
    def __init__(self, numeracao_do_aviao, nome_do_aviao, assentos_do_aviao):
        self.numeracao_do_aviao = numeracao_do_aviao
        self.nome_do_aviao = nome_do_aviao
        self.assentos_do_aviao = assentos_do_aviao

lista_aviao = []
lista_clientes = []
contador_aviao = 0

while True:

    opcao = menu_aviao()

    if opcao == 1:
        cadastrar_aviao()

    elif opcao == 2:
        exibir_informacoes()

    elif opcao == 0:
        sair()
        break
    else:
        print("Escolha uma opção Válida! Tente Novamente!")