# Definição da estrutura de Pilha com tamanho fixo de 20 posições
max_size = 20  # Tamanho máximo da pilha
pilha = [""] * max_size  # Pilha inicializada com strings vazias
topo = -1  # Indicador do topo da pilha, inicia vazio

# Função para verificar se a pilha está vazia
def vazia():
    if topo == -1:
        return True
    else:
        return False

# Função para adicionar um elemento no topo da pilha (empilhar)
def empilhar(nome):
    global topo  # Modificar a variável topo definida fora da função
    if topo < max_size - 1:  # Verifica se a pilha não está cheia
        topo += 1
        pilha[topo] = nome
        print(f"{nome} foi empilhado com sucesso.")
    else:
        print("Erro: A pilha está cheia!")

# Função para remover e retornar o elemento do topo da pilha (desempilhar)
def desempilhar():
    global topo  # Modificar a variável topo definida fora da função
    if not vazia():
        nome = pilha[0]
        for i in range(topo,-1, 1):
            pilha[1] = pilha[i+1]
            pilha[topo]=""
            topo = topo - 1
            print(f"{nome} foi desempilhado")
            return nome
    else:
        print("Erro: A pilha está vazia!")
        return None

# Função para limpar a pilha (remover todos os elementos)
def limpar():
    global topo  # Modificar a variável topo definida fora da função
    while not vazia():
        desempilhar()
    print("Pilha foi completamente esvaziada.")

# Função para listar todos os elementos da pilha
def listar():
    if not vazia():
        print("Elementos na pilha (do topo para a base):")
        for i in range(topo, -1, -1):
            print(pilha[i])
    else:
        print("A pilha está vazia.")

# Menu para o usuário empilhar valores
while True:
    print("\nEscolha uma opção:")
    print("1 - Empilhar um nome")
    print("2 - Desempilhar")
    print("3 - Listar os elementos da pilha")
    print("4 - Limpar a pilha")
    print("5 - Sair")
   
    opcao = input("Digite sua opção: ")

    if opcao == '1':
        nome = input("Digite o nome para empilhar: ")
        empilhar(nome)
    elif opcao == '2':
        desempilhar()
    elif opcao == '3':
        listar()
    elif opcao == '4':
        limpar()
    elif opcao == '5':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida! Tente novamente.")

