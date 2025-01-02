fila = []

def saudacoes():
    print("--"*30)
    print("Sejam Bem vindos (a) ao Sistema!")
    print("--"*30)

def exibirmenu():
    print("--"*30)
    print("1 - Adicionar elemento a Fila")
    print("2 - Remover o elemento no início da Fila")
    print("3 - Limpar Lista")
    print("4 - Listar Todos elementos da Lista")
    print("5 - Checar se a Lista está Vazia")
    print("6 - Sair do Sistema")
    opcao = int(input("Escolha uma opção: "))
    print("--"*30)
    return opcao

def adicionar():
    print("--"*30)
    nome = input("Digite o nome de um elemento para adicionar a lista: ")
    fila.append(nome)
    print(f"{nome} adicionado a lista!")
    print("--"*30)

def remover():
    if fila:  # Verifica se a fila não está vazia
        print("--"*30)
        remove = fila.pop(0)
        print(f"O elemento {remove} foi removido com sucesso!")
        print("--"*30)
    else:
        print("--"*30)
        print("A fila está vazia, não é possível remover.")
        print("--"*30)

def limpar():
    print("--"*30)
    fila.clear()
    print("Todos elementos removidos com sucesso!")   
    print("--"*30)

def listar():
    print("--"*30)
    print("Todos os elementos adicionados a lista:")
    for filas in fila:
        print(filas)
    print("--"*30)

def vazio():
    if not fila:  # Verifica se a fila está vazia
        print("--"*30)
        print("A lista está vazia!")
        print("Falso")
        print("--"*30)
        return True
    else:
        print("--"*30)
        print("A lista está com itens")
        print("Verdadeiro")
        print("--"*30)
        return False

def sair():
    print("--"*30)
    print("Saindo do Sistema...")
    print("--"*30)

def erro():
    print("Opção Inválida! Tente Novamente!")

saudacoes()

while True:
    opcao = exibirmenu()

    if opcao == 1:
        adicionar()
    elif opcao == 2:
        remover()
    elif opcao == 3:
        limpar()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        vazio()
    elif opcao == 6:
        sair()
        break 
    else:
        erro()

        # Usando novo conceito aprendido nesta atividade
