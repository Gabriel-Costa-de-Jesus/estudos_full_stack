# Sintaxe básica
def minhaprimeirafuncao():
    print("Minha primeira função!")

minhaprimeirafuncao() # Chamando a função

# Exemplo prático

def funcaotexto(nome):
    print("Seja bem vindo (a)!", nome)

funcaotexto("Ana")
funcaotexto("Matheus")
funcaotexto("Gabriel")

# Exemplo 2 com duas variáveis
def saudacao(saudacao1, nome):
    print(saudacao1, nome)

saudacao("Bom dia", "Ana")
saudacao("Boa tarde", "Matheus")
saudacao("Boa noite", "Miguel")

# Função com 2 argumentos (Usuário que manda)
def ola(nome,sobrenome):
    print(f"Olá {nome} {sobrenome} muito prazer em te conhecer")

nome = input("Qual é seu nome? ")
sobrenome = input("Qual seu sobrenome? ")

ola(nome,sobrenome)