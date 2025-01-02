class Dados:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

def menu():
    print("1- Adicionar")
    print("2 - Calcular")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    return opcao

def adicionar(lista_pessoas):
    nome = input("Digite o nome da pessoa: ")
    idade = input("Digite a idade da pessoa: ")
    dadosgerais = Dados(nome, idade)
    lista_pessoas.append(dadosgerais)
    print(f"Nome: {dadosgerais.nome} Idade: {dadosgerais.idade}")

def calcular(lista_pessoas):
    print("Lista de pessoas cadastradas:")
    for pessoa in lista_pessoas:
        print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")

def sair():
    print("Saindo do sistema...")

# Lista para armazenar múltiplas pessoas
lista_pessoas = []

# Pegando o limite de pessoas
limite = int(input("Digite a quantidade de pessoas: "))

# Loop para adicionar pessoas ou calcular, dependendo da opção
for i in range(limite):
    opcao = menu()  # Pegando a opção a cada iteração do loop

    if opcao == 1:
        adicionar(lista_pessoas)
    elif opcao == 2:
        calcular(lista_pessoas)
    elif opcao == 3:
        sair()
        break
    else:
        print("Opção inválida. Tente novamente.")
