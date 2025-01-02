print("Seja bem vindo (a) ao programa!")
print("Insira um número positivo, ao inserir um número negativo o programa fechará")

numero = int(input("Digite um número: "))
soma = 0

while (numero >= 0):
#    soma = numero+numero ao fazer dessa forma o programa só soma até o segundo número, não é correto fazer isso
   soma += numero #Forma correta de se fazer
   numero = int(input("Digite outro número: "))  
   if (numero < 0):
        print("Soma dos números positivos", soma)
        print("Programando encerrado")
        break
