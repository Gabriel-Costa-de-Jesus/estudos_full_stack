# Função que calcula e retorna a média entre dois números.
def media(n1, n2):
    return n1 / n2

resultado = media(10, 5)
print(resultado)


# Função ARGS: permite receber vários argumentos em uma única variável, armazenados como uma tupla.
# Os elementos podem ser acessados por meio de seus índices (posições).

def funcaoargs(*frutas):
    print("Eu gosto de:", frutas[0])
    print("Eu gosto de:", frutas[1])
    print("Eu gosto de:", frutas[2])

funcaoargs("Banana", "Maçã", "Morango")

# Da para usar o args em listas para unilas
def unirlista(*listas):
    print(listas)

lista1 = [1,2,3]
lista2 = [4,5,6]

unirlista(*lista1,*lista2)

# Função com **kwargs: permite passar vários argumentos nomeados (como um dicionário).
# Esses argumentos são armazenados como pares de chave e valor.
def funcaokargs(**parametros):
    print("Eu moro em", parametros["cidade1"])

# Chamada da função com argumentos nomeados
funcaokargs(cidade1="SP", cidade2="RJ")

x: str = 10 
y: int = 5

resultado = x + y
print(resultado)