litro_da_gasolina = 6.27  # Preço atual da gasolina 06/11/2024
valor_pagamento = input("Digite o valor do pagamento em reais: ")

# Remove o 'R$', espaços extras e troca a vírgula por ponto
valor_pagamento = valor_pagamento.replace("R$", "").replace(" ", "").replace(",", ".")

# Converte para float
valor_pagamento = float(valor_pagamento)

litros = valor_pagamento / litro_da_gasolina
print(f"Total de litros colocados: {litros:.2f} litros")


'''
5. Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o
preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no
tanque. 
'''