try:
    idade = int(input("Digite a sua idade: "))

    if (idade > 0 and idade <= 2):
        print(f"Você tem {idade} anos de idade, você é um bebê")

    elif (idade >= 3 and idade <= 12):
        print(f"Você tem {idade} anos de idade, você é uma criança")

    elif (idade >= 13 and idade <= 19):
        print(f"Você tem {idade} anos de idade, você é um adolescente")

    elif (idade >= 20 and idade <= 59):
        print(f"Você tem {idade} anos de idade, você é um adulto")

    elif (idade >= 60 and idade < 100):
        print(f"Você tem {idade} anos de idade, você é um idoso")

    elif (idade >= 100):
        print(f"Você tem {idade} anos de idade, você é a rainha Elizabeth")

    elif (idade <= 0 ):
        print("Você está morto!")

except ValueError:
     print("Por favor, digite apenas números inteiros.")
"""
Escreva um programa que solicite ao usuário para inserir uma idade e
verifique se a pessoa é um bebê (0 a 2 anos), criança (3 a 12 anos),
adolescente (13 a 19 anos), adulto (20 a 59 anos) ou idoso (60 anos ou mais).
"""