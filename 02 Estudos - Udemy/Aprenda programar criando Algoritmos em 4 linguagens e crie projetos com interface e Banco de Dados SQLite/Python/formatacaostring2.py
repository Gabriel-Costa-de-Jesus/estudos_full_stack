nome = "       Gabriel Costa de Jesus      "
print(nome)
print(nome.strip()) #Remove os espaços da palavra inicial

# Procurando palavras

gosto_frutas = "Eu gosto de MAÇA"

print("Maça" in gosto_frutas) # Ele procura uma palavra dentro de uma variavel, letra maiscula e minuscula e espaço faz diferença e retorna true se achar
print("maça" in gosto_frutas.lower()) # Retornou true porque botei a palavra minuiscula

#o find procura e retorna o indice(posição da letra)

resultado = gosto_frutas.find("u")
print(resultado)

# Verifica se uma palavra não está presente dentro de uma variável
copa = "O Brasil ganhou a copa"
campeao = "Alemanha" not in copa 
print(campeao)

campeao = "Brasil" not in copa 
print(campeao)

# Exibir casas decimias

n1 = 24.123456
print(f"{n1:.2f}") # Tem que colocar dentro de {} e com f para funcionar