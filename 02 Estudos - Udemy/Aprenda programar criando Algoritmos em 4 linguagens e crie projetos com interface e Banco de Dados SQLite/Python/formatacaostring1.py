nome = "Gabriel Costa de Jesus"
print(nome)
print("Total de caracteres:" + str(len(nome))) #Conta os caracteres do nome que é 22

print(nome[0]) # Retorna o primeiro valor da variavel que é G
print(nome[8:13]) # Retornando uma pequena parte COSTA

# UPPER Retorna todas as letras em maiúscula
print(nome.upper())
# Lower Retorna minúsculo
print(nome.lower())

# Replace troca as palavras, substitui
print(nome.replace("Costa", "Machado"))

# Separar uma string por partes
cpfex = "01230.456.789-10"

cpf_parte = cpfex.split("0") # Separando com 0
print(cpf_parte)

cpf = "123.456.789-10"
cpf_parte = cpf.split(".") # Separando com .
print(cpf_parte)
print(cpf_parte[0]) # Mostrando a parte 0 que está separada
print(cpf_parte[1])

cpf_parte2 = cpf_parte[2].split("-")
print(cpf_parte2[0])
print(cpf_parte2[1])