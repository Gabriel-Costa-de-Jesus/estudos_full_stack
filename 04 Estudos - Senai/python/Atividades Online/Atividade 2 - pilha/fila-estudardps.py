# Definição da estrutura de Fila com tamanho fixo de 20 posições
max_size = 20  # Tamanho máximo da fila
fila = [""] * max_size  # Fila inicializada com strings vazias
inicio = 0  # Indicador do início da fila
fim = -1  # Indicador do fim da fila
tamanho_atual = 0  # Tamanho atual da fila

# Função para verificar se a fila está vazia
def vazia():
    return tamanho_atual == 0

# Função para verificar se a fila está cheia
def cheia():
    return tamanho_atual == max_size

# Função para adicionar um elemento no fim da fila (enfileirar)
def enfileirar(nome):
    global fim, tamanho_atual
    if not cheia():
        fim = (fim + 1) % max_size  # Aumenta o fim e o mantém dentro dos limites da fila circular
        fila[fim] = nome
        tamanho_atual += 1
        print(f"{nome} foi enfileirado com sucesso.")
    else:
        print("Erro: A fila está cheia!")

# Função para remover e retornar o elemento do início da fila (desenfileirar)
def desenfileirar():
    global inicio, tamanho_atual
    if not vazia():
        nome = fila[inicio]
        fila[inicio] = ""  # Remove o valor do início
        inicio = (inicio + 1) % max_size  # Avança o início e o mantém dentro dos limites da fila circular
        tamanho_atual -= 1
        print(f"{nome} foi desenfileirado.")
        return nome
    else:
        print("Erro: A fila está vazia!")
        return None

# Função para listar todos os elementos da fila
def listar():
    if not vazia():
        print("Elementos na fila (do início para o fim):")
        index = inicio
        for _ in range(tamanho_atual):
            print(fila[index])
            index = (index + 1) % max_size
    else:
        print("A fila está vazia.")

# Função para limpar a fila (remover todos os elementos)
def limpar():
    global inicio, fim, tamanho_atual
    inicio = 0
    fim = -1
    tamanho_atual = 0
    print("Fila foi completamente esvaziada.")

# Menu para o usuário enfileirar e desenfileirar valores
while True:
    print("\nEscolha uma opção:")
    print("1 - Enfileirar um nome")
    print("2 - Desenfileirar")
    print("3 - Listar os elementos da fila")
    print("4 - Limpar a fila")
    print("5 - Sair")
   
    opcao = input("Digite sua opção: ")

    if opcao == '1':
        nome = input("Digite o nome para enfileirar: ")
        enfileirar(nome)
    elif opcao == '2':
        desenfileirar()
    elif opcao == '3':
        listar()
    elif opcao == '4':
        limpar()
    elif opcao == '5':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida! Tente novamente.")
