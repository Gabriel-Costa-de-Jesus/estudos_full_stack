# VAlor Min e Max
lista = [1, 5, 3, 10, 20, 15]

print(min(lista)) # Imprime o menor valor da lista
print(max(lista)) # Imprime o maior valor da lista

# Uma forma de fazer uma lista
listade1ate100 = [posicao for posicao in range(101)]
print(listade1ate100)

print("\n")

# Colocando uma condicional

listade1ate10 = [posicao for posicao in range(100) if posicao <= 10] # Imprima enquanto a posicao <= 10
print(listade1ate10)

listateste = [posicao for posicao in range(11) if posicao == 5] # Imprima se a posicao for igual a 5
print(listateste)

# Lista com for range

pulandode2em2 = list(range(2,20,2))
print(pulandode2em2)

# Juntando listas

listaoriginal = ["Carro", "Cerveja", "Piscina", "Churrasco"]
listacopiada = listaoriginal.copy() # Copiando a lista

print(listacopiada)

lista1 = ["A", "B", "C"]
lista2 = [1, 2, 3]

listajunta = lista1 + lista2
print(listajunta)

# Outra forma de juntar

l1 = ["Fruta", "CArro", "Bola"]
l2 = [10, 20, 30]

# Forma errada que fiz, pois ele adiconou a lista inteira em apenas um espaço da lista ao invés de reservar um normal
# Por isso o professor do vídeo usou o for para armazenar individualmente, vez por vez
l1.append(l2)
print(l1)
print(l1[3]) 

l1.pop(3)
print(l1)

for posicao in l2: # O for passa um dado da lista por vez para a variavel posicao, e logo após adiciona em l1
# Logo após manda para l1
    l1.append(posicao)
print(l1)
print(l1[4:6]) # AGora está certo