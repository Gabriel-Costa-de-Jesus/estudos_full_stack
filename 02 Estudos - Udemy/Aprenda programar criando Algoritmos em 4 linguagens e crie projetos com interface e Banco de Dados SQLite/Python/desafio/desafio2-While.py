'''
Exercício: Praticando a Estrutura de Controle While em Python



Neste exercício, você vai criar um programa que simula um relógio contando de 0 a 60 segundos usando o While.



Primeiro, crie uma variável chamada segundos e atribua a ela o valor 0. Esta variável irá representar os segundos no relógio.

Em seguida, crie uma estrutura de controle while que continuará executando enquanto o valor de segundos for menor ou igual a 60.

Dentro do loop while, imprima o valor atual de segundos, então incremente o valor de segundos em 1. Você pode incrementar o valor de segundos em Python com segundos += 1.

Seu programa deve imprimir cada segundo do relógio de 0 a 60, um por linha.



Boa sorte!
'''
import time

segundos = 0

while segundos <= 60:
    print(f"Segundos ({segundos})")
    segundos += 1
    time.sleep(1)