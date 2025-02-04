# Dicionario serve para organizar os dados
dicionario = {
    "Ana": 25,
    "Mateus": 30,
    "Julio":18
}

print(dicionario) # Imprimindo o dicionario
print(len(dicionario)) # Imprimindo a quantidade de linha do dicionario
print(type(dicionario)) # Imprimindo o tipo do dicionario

print(" ")

# Copiando o dicionario
dicionario2 = dicionario.copy()
print(dicionario2)

print(' ')

# Outra forma de copiar, tipo convertendo
dicionario3 = dict(dicionario)
print(dicionario3)

# O dicionario sempre retorna o último item do valor duplicado como no exemplo abaixo
pessoas = {
    "Paulo": 30,
    "Gabriel": 20,
    "Gabriel": 19,
    "Marçal": 35,
}
print(pessoas)

# Pegando apenas o número do dicionario

dados = pessoas["Gabriel"]
dados2 = pessoas.get("Marçal")
print(dados)
print(dados2)

# Pegando todos os nomes
nome = pessoas.keys()
print(nome)

# Pegando todas as idades
idade = pessoas.values()
print(idade)

# ALterando informações do dicionario

alimentos = {
    "Macarrão": 10,
    "Carne": 30,
    "CarneVegana": 80
}

print(alimentos)

alimentos["Macarrão"] = 9
print(alimentos)

# Outra forma de trocar
alimentos.update({"Carne": 20})
print(alimentos)

print(" ")

# Adicionando alimentos
alimentos["Salsicha"] = 25
print(alimentos)

# REmovendo alimentos
alimentos.pop("Salsicha")
print(alimentos)

# Outra forma de remover por indice
alimentos.popitem()
print(alimentos)

# Apagando tudo
alimentos.clear()
print(alimentos)

# Adicionando novamente
alimentos["Arroz"] = 23
alimentos["Abobora carne de petista"] = 30
alimentos["Feijão"] = 12

print(alimentos)

# Apagando com DEL

del alimentos["Arroz"]
print(alimentos)

# Verificando palavras no dicionario
if "Feijão" in alimentos:
    print("Feijão encontrado")

# Imprimindo com for

letras = {
    "A": 2,
    "B": 5,
    "C": 7,
    "D": 0,
    "E": 9
}

# Imprimindo os nomes
for posicao in letras:
    print(posicao)

print(" ")

# Imprimindo os valores
for i in letras:
    print(letras[i])

print(" ")

# Imprimindo os valores 2
for contador in letras.values():
    print(contador)

for titulo, valor in letras.items():
    print(f"{titulo} - {valor}")

#----------------------------------

print("\n\n")

escola = {
    "Turma 1" : {
        "Andre:" : 10,
        "Amanda:" : 8
    },
    "Turma 2" : {
        "Cesar:" : 6,
        "Alessandra:" : 7
    },
    "Turma 3" : {
        "Roger:" : 9,
        "Rosiane:" : 10
    }
}

for tur1, tur2 in escola.items():
    print(tur1)
    for tur1, tur2 in tur2.items():
        print("Aluno:", tur1, "- Nota:", tur2)


