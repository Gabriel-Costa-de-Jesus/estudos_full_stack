# Ordenando listas Alfabéticas
lista = ["A", "C", "E", "D", "B", "F", "G"]
print(lista)

lista.sort() # ORdenando de A a Z
print(lista)

lista.sort(reverse=True) # ORdenando de Z a A
print(lista)

print("\n")

# Ordenando listas Númericas
lista2 = [1,3,2,4,6,5]
print(lista2)

lista2.sort() # ORdenando de A a Z
print(lista2)

lista2.sort(reverse=True) # ORdenando de Z a A
print(lista2)

print("\n")

#Maiuscula e Minusca 
listaMaiMin = ["Sofá", "tv", "carro", "Casa", "Armario"]
listaMaiMin.sort() 
print(listaMaiMin)

listaMaiMin.sort(key= str.lower) # Para ordenar corretamente todas devem estar iguais, ou maiusculo ou minusculo
print(listaMaiMin)
