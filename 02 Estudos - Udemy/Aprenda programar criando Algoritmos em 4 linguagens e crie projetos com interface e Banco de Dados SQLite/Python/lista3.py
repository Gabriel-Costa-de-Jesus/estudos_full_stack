l1 = ["A", "B", "C"]
l2 = ["D", "E", "F"]

l1.extend(l2)
print(l1) # Forma de juntar listas sem dar erro

l1.remove("B") # Remover item da lista com base no nome
print(l1)

l1.pop(3) # REmove com base no indice
print(l1)

l1.pop() # Por padrão remove o ultimo da lista
print(l1)

del l1[0] # Outra forma de remover da lista
print(l1)

l1.clear() # Remove toda a lista
print(l1)

# Adicionando itens a lista

l1.append("Carro") # Adicionando na lista
print(l1)

l1.insert(1, "Moto") # Adiciona com base na posição (indice)
print(l1)

l1.insert(1, "Avião") # Se adiciona o item na mesma posição o outro item passa para a segunda posição (Empurra)
print(l1)

# Checando se tem a palavra na lista

if "Carro" in l1: # Pergunta se existe carro em l1
    print("Sim, existe Carro na lista")
else:
    print("Não existe na lista")

# Trocando um item da lista

l1[2] = "Barco"
print(l1)

# Alterando de uma posicao inicial até final

l1[0:2] = ["Metrô", "Trêm"]
print(l1)