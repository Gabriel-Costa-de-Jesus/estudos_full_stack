lista = ["Amanda", "Bernado", "Camila", "Daniel", "Emanuel", "Felipe", "Gabriel"]

# Impressão normal
for i in lista:
    print(i)

print("\n")

# ShortHand
[print(posicao) for posicao in lista]

print("\n")

# Impressão com While
i = 0
while i < len(lista):
    print(lista[i])
    i += 1

print("\n")

# Procurando item numa lista e adicionando em outra
novalista = []
for procurar in lista:
    if "C" in procurar:
        print(f"{procurar} Adicionado a nova lista!")
        novalista.append(procurar)
        print(novalista)

# Deixando os itens da lista em maiúsculo e minúsculo

# Lista original
lista2 = ['maçã', 'banana', 'laranja', 'uva']

# Nova lista2 com os itens em maiúsculas
lista_maiuscula = [item.upper() for item in lista2]

print("Lista original:", lista2)
print("Lista em maiúsculas:", lista_maiuscula)

# Nova lista2 com os itens em minusculo
lista_minusculo = [item.lower() for item in lista2] # item é uma variável temporaria apenas para guardar e passar os valores

print("Lista original:", lista2)
print("Lista em maiúsculas:", lista_minusculo)
