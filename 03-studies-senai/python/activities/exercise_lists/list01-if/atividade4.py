letra = input("Digite uma letra: ").upper()  # O upper converte a letra para maiúscula para facilitar a comparação

# Verifica se a letra está entre as vogais, Desta forma consigo colocar uma pequena lista de variáveis
if letra in ["A", "E", "I", "O", "U"]: # Verifica se tem determinada letra dessa lista com a letra que escrevir em letra
    print("Esta letra é uma Vogal")
else:
    print("Esta letra é uma Consoante")

"""
Escreva um programa que solicite ao usuário para inserir um caractere e
verifique se é uma vogal ou uma consoante.
"""
