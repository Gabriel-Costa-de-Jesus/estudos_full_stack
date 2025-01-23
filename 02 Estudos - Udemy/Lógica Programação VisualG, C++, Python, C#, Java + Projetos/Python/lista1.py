# Lista Padrão
lista = ["Banana", "Maça", "Uva", "Perâ", "Morango", "Pêssego", "Kiwi", "Laranja"]

print(lista)
print(len(lista)) # Len tamanaho da lista
print("\n")

# " Imprimindo de acordo com a posição da lista"
print(lista[0])
print(lista[1])
print(lista[2])

print("1",lista[-1]) #Imprime o último da lista
print("2",lista[0:3]) # Imprime da posição 0 a 3
print("3",lista[:3]) # Imprime os trÊs primeiros
print("4",lista[2:]) # Imprime a partir dos terceiro item
print("5",lista[::2]) # Imprime de 2 em 2

print("\n")
# Usando a cabeça pra facilitar
i = 7
for posicao in lista:
    print(lista[i])
    i -= 1

print("\n")  

# -1 Equivale a última posição da Lista
y = -1
for posicao in lista:
    print(lista[y])
    y -= 1