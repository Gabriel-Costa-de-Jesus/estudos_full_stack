# Criando Classe
class Informacoes_dados: # A Classe serve para agrupar informações(Dados) facilita a manutenção do código
    nome = "João"
    idade = 30

pega_idade = Informacoes_dados() # Tem que instanciar um objeto para pegar a Class e fazer contato
print(pega_idade.nome)
print(pega_idade.idade)

# Passando dados para uma CLass
class Turma1:
    nome = ""
    idade = 0
    altura = 0

dados_da_turma = Turma1()
dados_da_turma.nome = "Cintia"
dados_da_turma.idade = 20
dados_da_turma.altura = 1.72

print(dados_da_turma.nome, dados_da_turma.idade, dados_da_turma.altura)

# Usando o self, o self serve para pegar dados dentro da class
class Turma:
    def __init__(self, nome,idade,altura):
        self.nome_do_aluno = nome
        self.idade_do_aluno = idade
        self.altura_do_aluno = altura
    
    def imprimir(self):
        print("------------------------------")
        print(f"Aluno: {self.nome_do_aluno}")
        print(f"Idade: {self.idade_do_aluno}")
        print(f"Altura: {self.altura_do_aluno:.2f}")
        print("------------------------------")

# Conectando a Class
aluno1 = Turma("Gabriel", 19, 1.75)
aluno2 = Turma("Alessandra", 19, 1.65)
aluno3 = Turma("Lucas", 20, 1.90)

aluno1.imprimir()
aluno2.imprimir()
aluno3.imprimir()