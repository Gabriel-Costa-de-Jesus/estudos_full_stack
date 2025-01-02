class Usuario:
    def __init__(self, nome, idade, data_nascimento):
        self.nome = nome
        self.idade = idade
        self.data_nascimento = data_nascimento

usuarioJose = Usuario("José", 30, "10/10/2020")
usuarioMaria = Usuario("Maria", 18, "10/10/2005")
usuarioIsac = Usuario("Isac", 20, "10/10/2000")

lista_usuarios = [usuarioJose, usuarioMaria, usuarioIsac]

for usuario in lista_usuarios:
    print("Nome", usuario.nome)
    print("Idade", usuario.idade)
    print("Data Nascimento", usuario.data_nascimento)
    print()
    