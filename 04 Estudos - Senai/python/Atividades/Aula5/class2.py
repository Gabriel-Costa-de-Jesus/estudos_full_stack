class Usuario: # Classe para organizar os dados
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

usuarios = [] #Lista para armazenar o nome e a idade dos usuários

nome = input("Informe o nome da pessoa") # armazenar o usuario dentro da class
idade = input("informe a idade") # armazenar a idade dentro da class

usuario = Usuario(nome, idade) #Criou uma variavel para conectar os dados que estão dentro da class, essa variável vai armazenar o nome e a idade que estão na class #Instanciou

usuarios.append(usuario) # Armazenou os dados dentro da lista

for junto in usuarios:
    print(junto)
        