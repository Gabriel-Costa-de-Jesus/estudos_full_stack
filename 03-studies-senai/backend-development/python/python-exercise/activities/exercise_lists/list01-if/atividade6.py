try:
    mes = int(input("Digite o número de um Mês: "))

    if (mes == 1):
        print("Este mês é Janeiro")

    elif (mes == 2):
        print("Este mês é Fevereiro")

    elif (mes == 3):
        print("Este mês é Março")

    elif (mes == 4):
        print("Este mês é Abril")

    elif (mes == 5):
        print("Este mês é Maio")

    elif (mes == 6):
        print("Este mês é Junho")

    elif (mes == 7):
        print("Este mês é Julho")

    elif (mes == 8):
        print("Este mês é Agosto")

    elif (mes == 9):
        print("Este mês é Setembro")

    elif (mes == 10):
        print("Este mês é Outubro")

    elif (mes == 11):
        print("Este mês é Novembro")

    elif (mes == 12):
        print("Este mês é Dezembro")
    else:
        print("Por favor, Insira um número correspondente ao mês!")   

except ValueError:
    print("Por favor, digite apenas números inteiros.")

""""
Escreva um programa que solicite ao usuário para inserir um número de mês
(1 a 12) e imprima o nome do mês correspondente.
"""
