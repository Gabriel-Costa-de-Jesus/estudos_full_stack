'''
Crie uma lista chamada frutas que contenha as seguintes strings: "maçã", "banana", "manga", "abacate" e "laranja".

Adicione a string "kiwi" ao final da lista frutas.

Remova a string "banana" da lista frutas.

Verifique se a string "abacaxi" está na lista frutas. Imprima "Abacaxi está na lista" se estiver, ou "Abacaxi não está na lista" se não estiver.

Use a função len() para imprimir o número de frutas na lista frutas.

Imprima o nome da primeira fruta e da última fruta na lista.



Este exercício tem como objetivo ajudá-lo(a) a praticar as operações básicas com listas em Python, como adicionar elementos, remover elementos, verificar a presença de um elemento, obter o comprimento da lista e acessar elementos em determinados índices.



Instruções para o Exercício de Listas em Python



Neste exercício, você estará trabalhando com listas em Python. A lista é uma das estruturas de dados mais usadas em Python e é importante entender como manipulá-las corretamente. Você estará usando uma lista de frutas para realizar várias operações.



Criação de Lista: Comece criando uma lista chamada frutas contendo as seguintes strings: "maçã", "banana", "manga", "abacate" e "laranja". Lembre-se de que listas em Python são criadas usando colchetes [] e os elementos são separados por vírgulas.

Adicionando Elementos: Adicione a string "kiwi" ao final da lista frutas. Em Python, você pode usar o método append() para adicionar um elemento ao final de uma lista.

Removendo Elementos: Remova a string "banana" da lista frutas. Para fazer isso, use o método remove(). Este método remove a primeira ocorrência do elemento especificado.

Verificando a Presença de um Elemento: Verifique se a string "abacaxi" está na lista frutas. Se estiver na lista, imprima a frase "Abacaxi está na lista". Se não estiver na lista, imprima "Abacaxi não está na lista". O operador in pode ser usado para verificar a presença de um elemento em uma lista.

Obtendo o Tamanho da Lista: Imprima o número de frutas na lista frutas. A função len() retorna o número de elementos em uma lista.

Acessando Elementos: Finalmente, imprima o nome da primeira e da última fruta na lista. Lembre-se de que em Python, o índice de uma lista começa em 0, então o primeiro elemento é acessado usando frutas[0]. O último elemento pode ser acessado usando frutas[-1].

Quando tiver concluído todas estas operações, revise o seu código para garantir que não cometeu erros. Tente executar o seu código para verificar se está funcionando corretamente. Se você encontrar erros, tente depurar seu código para entender o que está dando errado.



Boa sorte!
'''

lista = ["maçã", "banana", "manga", "abacate" ,"laranja"]

lista.append("kiwi")
lista.remove("banana")

if "abacaxi" in lista:
    print("Tem Abacaxi nesta lista")
else:
    print("Não tem abacaxi nesta lista")

print(f"Total de Frutas da lista: {len(lista)}")

print(f"Primeira Fruta da lista: {lista[0]}")
print(f"Última fruta da lista: {lista[-1]}")