#def nomedafunção (nomedavariavelOpcional):
#    print("Aqui escreve o restante da funçãp")
# Quando chamar a função tem que dizer o valor da variável Exemplo
# def titulo(txt):
#print(txt)

# titulo("A variável TXT irá receber esse nome que escreve")

def botarlinha():
    print("--"*30)
    print(msg)
    print("--"*30)

msg = "Olá, mundo"

def somar(n1_e2, n2_e2):
    print("A soma de {} e {} é {}".format(n1_e2, n2_e2, n1_e2+n2_e2))
    resul = n1_e2 + n2_e2
    print("O resultado é", resul)

def titulo(txt):
    print(txt)

opcao = None
while (opcao != 0):
    print("Qual Exercício você deseja fazer?")
    print("0 - Sair")
    print("1 - Exercício 1")
    print("2 - Exercício 2")
    print("3 - Exercício 3")
    opcao = int(input("Escolha a opção desejada\n"))

    if (opcao == 1):
        print("==== Exercício 1 ====")
        botarlinha()
    elif (opcao == 2):
        print("==== Exercício 2 ====")
        somar(4,5)
 
    elif (opcao == 3):
        print("==== Exercício 3 ====")
        titulo("A variável TXT irá receber esse nome que escreve")

    elif (opcao == 0):
        print("Saindo do Programa...")

    else:
        print("Opção Inválida - Tente novamente")
    
