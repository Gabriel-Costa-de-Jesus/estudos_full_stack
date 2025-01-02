print("Olá! Vamos adicionar frutas à sua lista.")

# Lista para armazenar as frutas
frutas = []

# Pergunta ao usuário quantas frutas ele quer adicionar
quantidade = int(input("Quantas frutas você deseja adicionar? "))

# Adiciona as frutas na lista
for i in range(quantidade):
    fruta = input(f"Digite o nome da fruta: ")
    frutas.append(fruta)

# Imprime as frutas cadastradas
print("\nAs frutas que você escolheu são:")
for fruta in frutas:
    print(fruta)

# Pergunta se o usuário quer remover alguma fruta
remover = input("\nDeseja remover alguma fruta da lista? (sim/não) ").lower()

while remover == 'sim':
    fruta_remover = input("Digite o nome da fruta que deseja remover: ")
    if fruta_remover in frutas:
        frutas.remove(fruta_remover)
        print(f"\n{fruta_remover} foi removida da lista.")
    else:
        print("\nEssa fruta não está na lista.")
    
    # Pergunta novamente se o usuário deseja remover outra fruta
    remover = input("\nDeseja remover mais alguma fruta? (sim/não) ").lower()

# Exibe a lista final de frutas
print("\nAs frutas finais da sua lista são:")
for fruta in frutas:
    print(fruta)
