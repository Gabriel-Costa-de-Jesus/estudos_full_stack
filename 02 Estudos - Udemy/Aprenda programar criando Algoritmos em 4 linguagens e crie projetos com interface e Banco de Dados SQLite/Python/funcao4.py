# Variáveis de escopo e Global

# Variáveis de escopo sáo variáveis que são criadas ou recebem algum dado novo dentro de um escopo(função por exemplo), elas só tem aquele valor dentro da função, fora da função ela não tem nada

# Variáveis Globais elas tem o mesmo valor dentro e fora de uma função

# Variável Global
nome = "Gabriel"

def nomes():
    print(nome) 

nomes() # Irá imprimir o nome Gabriel

sobrenome = "Nada"
def sobrenomes():
    sobrenome = "Costa" # Valor alterado, não sofre modificação fora da função
    print(sobrenome)

print(sobrenome) # Não irá imprimir o sobrenome costa pois, costa só existiu dentro da função
sobrenomes() # Irá imprimir o nome costa

# Tornando uma variável de escopo em global (NÃO É RECOMENDADO)
def sobrenomes2():
    global sobrenome2
    sobrenome2 = "De Jesus"
    print(sobrenome2)

sobrenomes2() # Imprimindo normal
print(sobrenome2) # A variável agora passou a ser global e teve seu valor modificado