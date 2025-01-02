Tarefas = []
Contar_Tarefa = 0
def ExibirMenu():
    print("\n" + "--"*30)
    print("Escolha uma das opções abaixo: \n")
    print("1 - Adicionar uma tarefa")
    print("2 - Listar todas as tarefas")
    print("3 - Marcar uma Tarefa como concluída")
    print("4 - Remover uma tarefa")
    print("5 - Sair do programa")
    print("--"*30)

def AdicionarTarefa():
    print("--"*30)
    Nome_da_Tarefa = input("Digite o nome da tarefa para ser criada\nTarefa {}: " .format(Contar_Tarefa))
    Status_da_Tarefa = "Pendente"
    Tarefas_e_Status = TarefaClass(Nome_da_Tarefa, Status_da_Tarefa)
    Tarefas.append(Tarefas_e_Status)
    print("Tarefa criada com sucesso!")
    print("--"*30)

def ListarTarefas():
    if (Contar_Tarefa >= 1):
        print("--"*30)
        print("Tarefas Criadas:\n")
        
        for Tarefas_e_Status in Tarefas:
            print("Tarefa:", Tarefas_e_Status.Nome_da_Tarefa, "Status:",  Tarefas_e_Status.Status_da_Tarefa)

        print("--"*30)
    else:
        print("Nenhuma Tarefa Criada! Crie uma tarefa primeiro")

def ConcluirTarefa():
    print("--"*30)
    Concluir_a_Tarefa = input("Digite o nome da Tarefa para ser concluída \n")
    for Tarefas_e_Status in Tarefas:
        if (Concluir_a_Tarefa == Tarefas_e_Status.Nome_da_Tarefa):
           Tarefas_e_Status.Status_da_Tarefa = "Concluída"
           print("A Tarefa foi concluída com sucesso")
           break
    else:
         print("Digite o nome correto da Tarefa!")
    print("--"*30)
    
def RemoverTarefa():
    print("--"*30)
    Remover_a_Tarefa = input("Digite o nome da Tarefa para ser removida \n")
    for Tarefas_e_Status in Tarefas:
        if (Remover_a_Tarefa == Tarefas_e_Status.Nome_da_Tarefa):
         Tarefas.remove(Tarefas_e_Status)
         print("A Tarefa foi removida com sucesso")
         break
         
    else:
        print("Digite o nome correto da Tarefa!") 
    print("--"*30)

def Sair():
    print("Saindo do Programa...")

class TarefaClass:
    def __init__(self, Nome_da_Tarefa, Status_da_Tarefa):
        self.Nome_da_Tarefa = Nome_da_Tarefa
        self.Status_da_Tarefa = Status_da_Tarefa

print("\n" + "--"*30)
print("Olá seja bem vindo (a) ao nosso sistema de tarefas!")

while (True):

    ExibirMenu()
    opcao_menu = int(input("Escolha uma opção: \n"))

    if (opcao_menu == 1):
        Contar_Tarefa += 1
        AdicionarTarefa()
    elif (opcao_menu  == 2):
        ListarTarefas()
    elif (opcao_menu == 3):
        ConcluirTarefa()
    elif(opcao_menu == 4):
        RemoverTarefa()
    elif (opcao_menu == 5):
        Sair()
        break
    else:
        print("Opção Inválida! Tente Novamente")