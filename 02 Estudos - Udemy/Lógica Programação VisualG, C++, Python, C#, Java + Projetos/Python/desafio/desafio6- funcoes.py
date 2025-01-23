'''
Neste exercício, você vai criar uma função que calcula a média de uma lista de números.


Siga os passos abaixo para realizar este exercício:



Primeiro, defina uma função chamada calcula_media que recebe uma lista de números como argumento.

Dentro da função, use a função incorporada sum para somar todos os números da lista e a função len para obter a quantidade de números. Divida a soma pela quantidade para obter a média.

Retorne a média calculada.

Aqui está o esboço do código que você precisa preencher:



def calcula_media(numeros):
    # Calcule a média dos números e retorne o resultado


Por exemplo, se a função for chamada com a lista [1, 2, 3, 4, 5], ela deve retornar 3.0.



Este exercício tem como objetivo ajudá-lo(a) a praticar a definição e uso de funções em Python, bem como familiarizar-se com algumas funções incorporadas úteis (sum e len). Ao concluir este exercício, você deve ser capaz de criar funções que executam cálculos simples e retornam um resultado.

'''

def calcular_media(numeros):
    return sum(numeros) / len(numeros)

# Chamando a função com uma lista de números
resultado = calcular_media([10, 20])
print(resultado)
