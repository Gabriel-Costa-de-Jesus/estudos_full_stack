from abc import ABC, abstractmethod

# Classe base abstrata
class Funcionarios(ABC):
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass

    def descrever(self):
        return f"Funcionário: {self.nome}, Salário Base: R${self.salario_base:.2f}"

# Subclasse Gerente
class Gerente(Funcionarios):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_base + self.bonus

# Subclasse Vendedor
class Vendedor(Funcionarios):
    def __init__(self, nome, salario_base, vendas, comissao):
        super().__init__(nome, salario_base)
        self.vendas = vendas
        self.comissao = comissao

    def calcular_salario(self):
        return self.salario_base + (self.vendas * self.comissao / 100)

# Subclasse Estagiário
class Estagiarios(Funcionarios):
    def __init__(self, nome, horas_trabalhadas, valor_por_hora):
        super().__init__(nome, 0)  # Salário base não é usado aqui
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_por_hora = valor_por_hora

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_por_hora

# Funções do sistema
funcionarios = []

def menu():
    print("--" * 30)
    print("1- Cadastrar o funcionário")
    print("2- Calcular o salário")
    print("3- Exibir lista de funcionários")
    print("4- Sair")
    print("--" * 30)
    return int(input("Digite a sua opção: "))

def cadastrar_funcionario():
    print("--" * 30)
    print("1- Cadastrar Gerente")
    print("2- Cadastrar Vendedor")
    print("3- Cadastrar Estagiário")
    print("--" * 30)
    tipo = int(input("Escolha uma opção: "))

    nome = input("Digite o nome do funcionário: ")
    
    if tipo == 1:
        salario_base = float(input("Digite o salário base: "))
        bonus = float(input("Digite o bônus: "))
        funcionarios.append(Gerente(nome, salario_base, bonus))
    elif tipo == 2:
        salario_base = float(input("Digite o salário base: "))
        vendas = float(input("Digite o total de vendas: "))
        comissao = float(input("Digite a comissão (%): "))
        funcionarios.append(Vendedor(nome, salario_base, vendas, comissao))
    elif tipo == 3:
        horas_trabalhadas = int(input("Digite as horas trabalhadas: "))
        valor_por_hora = float(input("Digite o valor por hora: "))
        funcionarios.append(Estagiarios(nome, horas_trabalhadas, valor_por_hora))
    else:
        print("Opção inválida!")

    print(f"Funcionário {nome} cadastrado com sucesso!")

def calcular_salario():
    for funcionario in funcionarios:
        print(f"{funcionario.descrever()} | Salário Final: R${funcionario.calcular_salario():.2f}")

def exibir_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        for funcionario in funcionarios:
            print(funcionario.descrever())

def sair():
    print("Saindo do sistema...")

# Loop principal
while True:
    opcao = menu()
    if opcao == 1:
        cadastrar_funcionario()
    elif opcao == 2:
        calcular_salario()
    elif opcao == 3:
        exibir_funcionarios()
    elif opcao == 4:
        sair()
        break
    else:
        print("Opção inválida!")
