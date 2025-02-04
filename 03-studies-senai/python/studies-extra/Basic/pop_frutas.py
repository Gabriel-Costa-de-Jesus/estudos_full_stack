frutas = [] # Vetor para guardar mais de uma informação

tipos_de_frutas = "Maça" # Variável para adicionar para se conectar ao vetor para adicionar as informações
frutas.append(tipos_de_frutas) #Adicionando as informações declaradas na variável

frutas.append("Uva") # Outra forma de adiconar, porém é eu que escolho e não o usuário

tipos_de_frutas = input("Digite o nome de uma fruta: ") # Outra forma de adicionar, o usuário que escolhe
frutas.append(tipos_de_frutas) #Adicionando as informações declaradas na variável

print(frutas) # Mostrando todas as frutas na tela

# USANDO O POP PARA REMOVER OS DADOS

# O método POP serve para remover uma informação de uma lista, ele remove de acordo com a posição (Exemplo: 0, 1, 2, 3...), caso não seja especificado o que ele deve remover, ele sempre removerá por padrão o último item selecionado, igual como uma pilha de pratos

print("Usando o POP para remover as frutas")

tipos_de_frutas = frutas.pop() # Ele removerá a última fruta escolhida pelo usuário

print("Fruta Removida:",tipos_de_frutas) # Fruta removida

print(frutas) # Mostrando todas as frutas na tela

# Podemos escolher qual fruta ele poderá remover

tipos_de_frutas = frutas.pop(0)

print("Fruta Removida:",tipos_de_frutas) # Fruta removida

print(frutas) # Mostrando todas as frutas na tela

# Podemos criar uma variável específica para remover, dessa forma o código ficará mais limpo

tipos_de_frutas = "Perâ"
frutas.append(tipos_de_frutas)

print("Nova fruta adicionada:", tipos_de_frutas)
print(frutas)

print("Removendo a fruta:", tipos_de_frutas)
removedor_de_frutas = frutas.pop()

print("Fruta Removida:", removedor_de_frutas)
print(frutas)


