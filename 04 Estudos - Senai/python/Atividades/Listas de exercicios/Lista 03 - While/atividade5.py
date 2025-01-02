soma = 0
qtd_vezes = 0
while True:
    num = int(input("Digite um número! Para sair digite um número negativo: "))

    if num < 0:
        print("Você digitou um número negativo. Saindo do programa...")
        break
    else:
        print(soma, "+", num)
        soma += num
        print(f"Resultado: {soma}")
        qtd_vezes += 1  # Contador de entradas

if qtd_vezes > 0: # Para evitar que o usuário digite um número negativo logo no início
    print(f"A soma de todos os números é {soma}")
    print(f"A média dos números é: {soma / qtd_vezes}")
else:
    print("Nenhum número válido foi inserido.")




'''
5. Média de números:
- Escreva um programa que use um loop `do-while` para ler números inteiros do usuário
até que ele digite um número negativo, e então calcule e imprima a média desses números.

soma = 0
qtd_vezes = 0
while True:
    num = int(input("Digite um número! Para sair digite um número negativo: "))

    if (num < 0):
        print("Você digitou um número negativo. Saindo do programa...")
        break
    else:
        print(soma,"+", num)
        soma += num
        print(f"Resultado: {soma}")
        qtd_vezes += 1 # Quantidade de vezes que o código foi repetido

print(f"A soma de todos os números é {soma}")
print(f"A média do número é: {soma/qtd_vezes}")

'''
