def menu_aviao():
    print("--"*30)
    print("Escolha a opção desejada")
    print("1 - Cadastrar Avião")
    print("2 - Exibir Aviões Cadastrado nos Sistemas")
    print("3 - Sair")
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

def sair():
    print("Saindo do Sistema...")

class Class_aviao:
    def __init__(self, numeracao_do_aviao, nome_do_aviao, assentos_do_aviao):
        self.numeracao_do_aviao = numeracao_do_aviao
        self.nome_do_aviao = nome_do_aviao
        self.assentos_do_aviao = assentos_do_aviao

lista_aviao = []
contador_aviao = 0

while True:

    opcao = menu_aviao()

    if opcao == 1:
        cadastrar_aviao()

    elif opcao == 2:
        exibir_informacoes()

    elif opcao == 3:
        sair()
        break
    else:
        print("Escolha uma opção Válida! Tente Novamente!")