soma = 0  # Inicializa a soma como zero para acumular
while True:  # Loop que vai simular um 'do-while'
    numero = int(input("Digite um número para somar (ou 0 para sair): "))
    if numero == 0:
        print("Saindo...")
        break
    soma += numero  # Adiciona o número digitado ao total acumulado
    print(f"Soma parcial: {soma}")

print(f"A soma total de todos os números digitados é: {soma}")


'''
 Entrada de dados até o zero:
- Escreva um programa que peça ao usuário para digitar números até que ele digite zero.
Use um loop `do-while`.

soma = 1
opcao = 1
while opcao != 0:
    soma = int(input("Digite um número que farei uma soma! Digite 0 para sair. "))
    opcao = soma
    print(soma, "+", soma)
    soma += soma
    print(soma)

    if opcao == 0:
        print("Saindo...")

'''
