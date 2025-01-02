try:
    num = int(input("Digite  um número: "))
    if num % 2 == 0:
        print("Este número é par")
    else:
        print("Este número é impar")

except ValueError:
    print("Por favor escolha um número inteiro")