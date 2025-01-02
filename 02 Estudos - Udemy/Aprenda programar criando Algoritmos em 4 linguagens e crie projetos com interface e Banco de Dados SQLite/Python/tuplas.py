'''
Tuplas (tuple)
Imutabilidade: Ao contrário das listas, tuplas são imutáveis, ou seja, seus elementos não podem ser modificados após a criação. Isso é útil para armazenar dados que você deseja garantir que não serão alterados, como constantes.
Desempenho: Por serem imutáveis, tuplas consomem menos memória e, em algumas operações, são mais rápidas que listas. Isso faz delas uma boa opção quando você precisa de acesso rápido a dados constantes.
Integridade dos dados: A imutabilidade permite usá-las como chaves em um dicionário (algo que as listas não permitem).

'''

tupla = ("A", "B", "C", "D", "E", "F", "G")

print(tupla)
print(type(tupla))
print(tupla[1])
print(tupla[-1])

print("\n")

# Adicionando novos itens a tupla, só é possível colocando uma nova tuplas nele
novatupla = ("H",) # ATENÇÃO, só é considerado tupla quando tem uma virgula a mais
tupla += novatupla
print(tupla)

# Removendo novos itens da tupla

removetupla = list(tupla) # Cria uma lista para receber os itens da tupla
removetupla.remove("B")
tupla = tuple(removetupla) # Convertendo em tupla
print(tupla)

#Imprimindo itens da tupla
tuplaFrutas = ("Banana", "Abacaxi", "Laranja", "Maça")

#for = para
for item in tuplaFrutas:
    print(item)


