num = 2 # Excluiu o número 1 e 0 que não são primos
qtd_divisao = 0 # Quantidade de vezes que o número é dividido, sendo que primo é divisível até duas vezes
limite = 0 # Limite do While
num_vetor = [] # Armazenar todos os números primos

while limite < 99:
    for i in range(1, num+1, 1):
        resto = num%i
        print(f"{num} / {i} = {resto}")
        if resto == 0:
            qtd_divisao += 1

    if qtd_divisao == 2:
        print(f"O número {num} é primo")
        num_vetor.append(num)

    print("--"*70) # Separar com linha
    num += 1 # Próximo número (Incrementação)
    limite += 1 # Adicionando + 1 no Limite
    qtd_divisao = 0 # Dando reset na quantidade de divisão

print(f"Os números que são primos de 1 a 100 são: {num_vetor}")
   
'''
7. Números primos:
- Escreva um programa que encontre todos os números primos entre 1 e 100 usando um
loop `while`.

'''
