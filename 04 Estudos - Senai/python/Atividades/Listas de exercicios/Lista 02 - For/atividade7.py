valor_fatorial = int(input("Digite um número para calcular o fatorial: "))
multi = 1  # Iniciamos com 1 para o cálculo correto do fatorial

for i in range(1, valor_fatorial + 1):
    print(multi, "*", i)
    multi *= i

print(f"O valor fatorial é {multi}")


# Escreva um programa que calcule o fatorial de um número inteiro dado pelo usuário usando um loop for.