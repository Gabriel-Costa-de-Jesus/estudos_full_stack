frutas = []

frutas.extend(["Banana","Maça","Uva"]) # O método extend adciona mais informações com apenas uma linha de código, já o append uma só
frutas.append("Pera")
frutas.append("Cereja")
frutas.append("Carambola")
print(frutas)

# Usando o remove para remover as frutas, o Remove remove uma informação escolhida por nós( Exemplo: Remova Pedro, ele vai e remove Pedro), diferente do POP, ele não guarda a informação removida e não usa a posição (Indice) para remover, dessa forma o pop é muito melhor

frutas.remove("Uva")

print(frutas)

# Para remover uma fruta escolhida pelo usuário é mais complicado, pois ele não se baseia por indice, então terei que usar class para armazenar

escolha_Fruta = input("Digite o nome da fruta para ser removida: ") # O usuário irá escolher a fruta para ser removida

if (escolha_Fruta in frutas):
    frutas.remove(escolha_Fruta)
    print(f"Fruta removida {escolha_Fruta}")
    print(frutas)