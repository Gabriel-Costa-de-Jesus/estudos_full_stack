# Estrutura padrão do FOR
lista = ["Maça","Banana", "Perâ"]

for posicao in lista:
    print(f"Fruta: {posicao}")

# Pode imprimir a posição, numeração, indice

for indice, posicao in enumerate(lista):
    print(f"Posição da Fruta: {indice} Fruta: {posicao}")

# Pode ser usado para achar uma fruta tbm
procurar = str(input("Procure uma fruta: "))
for posicaofruta in lista:
    if procurar in lista: # Eu botei lista aqui porque se botasse procurar fruta, o for ia repetir desde o começo da lista e quando achasse banana ia parar, porque o for é pela posição, ele ia checar se naquela posição 0 tinha banana
        print(f"Fruta {procurar} achada")
        break
    else:
        print("Fruta não achada")
# Pode ser usado para imprimir letras

for lista in "Banana":
    print(lista)