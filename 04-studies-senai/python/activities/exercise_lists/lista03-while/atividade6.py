num_fibonacci = int(input("Digite um número fibonacci: "))
num_atual = 0
num_anterior = 1


while num_fibonacci > 0:
    resultado = num_atual + num_anterior  
    print(f" = {resultado}", end=" ")
    print(f"({num_atual} + {num_anterior})")  # 0 + 1 | 1 + 1
     
    num_atual = num_anterior # num atual = 1 | 
    num_anterior = resultado # = 1 |
   
    num_fibonacci -= 1 # Limitador

    #Na segunda vez o numero atual tem que ser 1
# um precisa se atualizar primeiro e o outro dps


# num anterior é a soma dos numeros antigos
# num atual tem que ser o numero antigo sem atualizar


'''
6. Sequência de Fibonacci:
- Escreva um programa que use um loop `while` para gerar e imprimir os primeiros `n`
números da sequência de Fibonacci, onde `n` é fornecido pelo usuário.

'''
