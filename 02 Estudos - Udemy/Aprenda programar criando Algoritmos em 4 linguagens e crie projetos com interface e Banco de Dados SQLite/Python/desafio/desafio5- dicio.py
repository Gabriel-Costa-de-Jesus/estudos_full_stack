'''
Primeiro, crie um dicionário chamado animais, onde as chaves serão os nomes dos animais e os valores serão seus respectivos sons. Por exemplo, você pode adicionar os pares chave-valor 'cão': 'latido', 'gato': 'miado', 'vaca': 'mugido'.

Após criar o dicionário, imprima o som do 'cão' utilizando o dicionário animais.


'''

animais = {
    "Cao" : "Latido",
    "Gato": "Miado",
    "Vaca": "Mugido" 
}
for i in animais:
    if "Cao" in i:
        som = animais.get("Cao")
        print(f"Nome do animal: {i}  Som do animal {som}")