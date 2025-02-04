valor_do_quilo = 12.00
quilo = input("Digite o KG do prato: ")

# Remove o 'R$', espaços e troca a vírgula por ponto
quilo = quilo.replace("R$", "").replace(" ", "").replace(",", ".")

# Converte para float
quilo = float(quilo)

# Calcula o valor total
total = valor_do_quilo * quilo

# Exibe o valor total com vírgula
total_formatado = f"{total:.2f}".replace(".", ",")
print(f"Valor total: R$ {total_formatado}")


'''
6. O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva um algoritmo
que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a
balança já desconte o peso do prato. 
'''