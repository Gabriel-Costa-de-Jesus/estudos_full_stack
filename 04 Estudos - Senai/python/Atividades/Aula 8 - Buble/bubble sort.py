numeros = [1, 7, 10, 9, 2, 3, 20, 18, 33, 90, 44, 34, 30, 21, 27, 5, 8, 99, 54, 68] # Lista para guardar as variáveis para por em ordem

for numeromax in range(len(numeros) - 1): #Ele vai até a capacidade máxima da lista, que nesse caso é 5 posições, e vai tirar 1 posição cada vez que for for acionado, ficando, 4,3,2 ,1 a capacidade máxima
    for primeironumero in range(len(numeros) - 1 - numeromax):
        if numeros[primeironumero] > numeros[primeironumero + 1]:
            numeros[primeironumero], numeros[primeironumero + 1 ] = numeros[primeironumero + 1], numeros[primeironumero]
print("Lista final ordenada:", numeros)

# O primeiro for repete a lista de números e vai diminuindo a capacidade máxima em cada repetição
# O segundo for repete as passadas, um número passando pelo outro, e vai diminuindo as passadas desse número, tbm diminui a repetição do primeiro for
# O if compara os dois números da lista, se o primeiro for maior que o outro eles trocam de posição