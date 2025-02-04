n1 = 10
n2 = 20
n3 = 15

# Operador and, permite acrescentar e até colocar mais uma condição
if n1 < n2 and n2 > n3:
    print(True)

usuario = "Gabriel"
senha = 123

if usuario == "Gabriel" and senha == 123:
    print(f"Usuário {usuario} Logado com Sucesso!")

# Operador OR, se pelo menos uma das condições forem atendidos ele retorna

if n1 == n2 or n2 > n3:
    print("Uma das condições foram atendidas VERDADEIRO")

# Operador not, NÃO

letra = ""
if not letra:
    print("Não tem letra na palavra not")

fruta = "Banana"
if not fruta in "Maça":
    print("Não tem Maça nesta palavra")
    
frutas = ["Banana", "Maça", "Uva"]
procurar = input("Procure se tem uma fruta nessa lista ") 

if procurar in frutas:
    print(f"Fruta {procurar} achada")
else:
    print("Fruta não achada")
if not procurar in frutas:
    print(f"Fruta {procurar} não achada")