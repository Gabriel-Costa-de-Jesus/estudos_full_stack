# Outra forma de passar um Valor para a função
def notas(nota1,nota2,nota3):
    print(nota1)

notas(nota1 = 5, nota2 = 6, nota3 = 3)

#------------------------------------

# Função Padrão 

def nomes(nome = "Python"): # Pyton é um nome padrão da função, caso não for chamada e passada algum valor ele irá retornar o nome python por padrão
    print(nome)

nomes("Ana")
nomes("Júlia")
nomes()
nomes("Gabriel")

# Passando dados de uma lista

def lista(numeros):
    print(numeros)
    for itens in numeros:
        print(itens)

numeros = [1,2,3,4,5,6,7,8,9,10]
lista(numeros)

# Multiplicando com função

def multi(numerorecebido):
    return 10 * numerorecebido

multi(5)
print(f"10 * 10 = {multi(10)}") # Outra forma de imprimir