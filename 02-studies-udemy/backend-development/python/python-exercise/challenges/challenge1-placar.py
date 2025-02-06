'''
Neste exercício, você vai criar um programa que vai classificar uma pontuação de um jogo. A pontuação será um número inteiro entre 0 e 100 (inclusive).



Primeiro, crie uma variável chamada pontuacao e atribua a ela um valor entre 0 e 100.



Utilize a estrutura de controle if-elif-else para classificar a pontuação do seguinte modo:

Se a pontuação for maior ou igual a 90, imprima "Sua classificação é A. Parabéns!"

Se a pontuação for maior ou igual a 80 e menor que 90, imprima "Sua classificação é B. Muito bom!"

Se a pontuação for maior ou igual a 70 e menor que 80, imprima "Sua classificação é C. Bom trabalho!"

Se a pontuação for maior ou igual a 60 e menor que 70, imprima "Sua classificação é D. Precisa melhorar!"

Se a pontuação for menor que 60, imprima "Sua classificação é F. Estude mais!"



Esperamos que este exercício te ajude a melhorar sua compreensão das estruturas condicionais em Python!

'''

pontuacao = int(input("Digite a classificação pontuada: "))

if pontuacao >= 90 and pontuacao < 100:
    print("Sua classificação é A. Parabéns!")

elif pontuacao >= 80 and pontuacao < 90:
    print("Sua classificação é B. Muito bom!")

elif pontuacao >= 70 and pontuacao < 80:
    print("Sua classificação é C. Bom trabalho!")

elif pontuacao >= 60 and pontuacao < 70:
    print("Sua classificação é D. Precisa melhorar!")

elif pontuacao < 60:
    print("Sua classificação é F. Estude mais!")

else:
    print("Por favor! digite uma pontuação entre 0 a 100!")