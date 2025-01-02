class escolapai:
    def __init__(self,nome,idade,sexo,media, situacao):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.media = media
        self.situacao = situacao
    
    def imprimir(self):
        print("--"*30)
        print(f"Nome do aluno: {self.nome}")
        print(f"Idade do aluno: {self.idade}")
        print(f"Sexo do aluno: {self.sexo}")
        print(f"Média do aluno: {self.media}")
        print(f"Situação do aluno: {self.situacao}")
        print("--"*30)

# Passando dados de uma classe para outra, tem que por a classe que quer herdar os dados entre ()
class escolafilho(escolapai):
    def __init__(self, nome, idade, sexo, n1,n2,n3,n4): # Mesmo que não for usar as variáveis nome, idade, tem que colocar, e as que forem usar, ao invés de dizer o nome como a media, tem que colocar o self no super
        self.media = (n1+n2+n3+n4) / 4 # Usa o self para poder se conectar a variável de cima(pai)

        if self.media >= 6:
            self.situacao = "Aprovado"
        else:
            self.situacao = "Reprovado"
        super().__init__(nome, idade, sexo, self.media, self.situacao) # Usa o super para conectar os mesmos dados para serem passados

filho1 = escolafilho("Gabriel", 19, "M", 10, 9, 8, 7)
filho2 = escolafilho("Ana", 24, "F", 4, 5, 7, 6)
filho1.imprimir()
filho2.imprimir()