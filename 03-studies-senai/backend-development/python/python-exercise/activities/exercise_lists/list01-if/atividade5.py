try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    n3 = int(input("Digite mais um número: "))

    if (n1 < n2 and n1 < n3):
        print(f"O número {n1} é o menor entre eles")
    elif (n2 < n1 and n2 < n3):
        print(f"O número {n2} é o menor entre eles")
    elif (n3 < n1 and n3 < n2):
        print(f"O número {n3} é o menor entre eles")
    else:
        print("Os números não são todos distintos ou há um empate entre os menores.")
except ValueError:
    print("Por favor, digite apenas números inteiros.")


"""
Escreva um programa que solicite ao usuário para inserir três números
inteiros e imprima o menor deles.
"""