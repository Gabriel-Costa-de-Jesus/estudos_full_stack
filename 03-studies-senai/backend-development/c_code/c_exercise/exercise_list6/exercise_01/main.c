#include <stdio.h>
#include <locale.h>
#include <string.h>
#include <time.h>
#include <unistd.h> // Para sleep()


#define MAX_ALUNOS 5
#define MAX_NOTAS 3

struct SystemSchool {
    char nome[50];
    int idade;
    int matricula;
    float nota[MAX_NOTAS];
}; struct SystemSchool sistema[MAX_ALUNOS];
int contador = 0;

int menu() {
    int opcao;
    printf("\nEscolha uma opção abaixo:");
    printf("\n1- Cadastrar Aluno");
    printf("\n2- Listar Alunos");
    printf("\n3- Lançar Nota");
    printf("\n4- Sair do Sistema");
    printf("\nOpção: ");
    scanf("%d", &opcao);
    while (getchar() != '\n'); // Limpar buffer do teclado
    return opcao;
}

void cadastramentoAluno() {
    if (contador >= MAX_ALUNOS) {
        printf("\nLimite de alunos atingido!\n");
        return;
    }
    
    printf("\nDigite o nome do aluno: ");
    fgets(sistema[contador].nome, 50, stdin);
    sistema[contador].nome[strcspn(sistema[contador].nome, "\n")] = '\0';

    printf("Digite a idade do aluno: ");
    scanf("%d", &sistema[contador].idade);
    while (getchar() != '\n');

    sistema[contador].matricula = (int)time(NULL) % 100000 + contador;
    
    for (int i = 0; i < MAX_NOTAS; i++) {
        sistema[contador].nota[i] = 0.0;
    }

    printf("\nAluno cadastrado com sucesso!\n");
    contador++;
}

void listarAlunos() {
    if (contador == 0) {
        printf("\nNenhum aluno cadastrado no sistema!\n");
        return;
    }

    printf("\nAlunos cadastrados:\n");
    for (int i = 0; i < contador; i++) {
        printf("\nAluno [%d]: %s", i + 1, sistema[i].nome);
        printf("\nIdade: %d", sistema[i].idade);
        printf("\nMatrícula: %d", sistema[i].matricula);

        printf("\nNotas: ");
        int temNota = 0;
        for (int j = 0; j < MAX_NOTAS; j++) {
            printf("%.2f ", sistema[i].nota[j]);
            if (sistema[i].nota[j] > 0) temNota = 1;
        }
        if (!temNota) {
            printf("\nAluno sem notas cadastradas.");
        }
        printf("\n");
    }
}

void lancarNota() {
    if (contador == 0) {
        printf("\nNenhum aluno cadastrado no sistema!\n");
        return;
    }

    listarAlunos();

    int matriculaBuscar;
    printf("\nDigite o código da matrícula para lançar notas: ");
    scanf("%d", &matriculaBuscar);

    for (int i = 0; i < contador; i++) {
        if (matriculaBuscar == sistema[i].matricula) {
            printf("\nDigite as notas do aluno %s:\n", sistema[i].nome);
            for (int j = 0; j < MAX_NOTAS; j++) {
                printf("Nota %d: ", j + 1);
                scanf("%f", &sistema[i].nota[j]);
            }
            printf("\nNotas cadastradas com sucesso!\n");
            return;
        }
    }
    printf("\nAluno não encontrado no sistema!\n");
}

void sair() {
    printf("\nSaindo do sistema");
    for (int i = 0; i < 5; i++) {
        printf(".");
        sleep(1);
    }
    printf("\nObrigado por utilizar nosso sistema!\n");
    sleep(2);
}

// Funções Auxiliáres
void erro() {
    printf("\nOpção inválida, tente novamente!\n");
}

void pressAnyKey() {
    printf("\nPressione Enter para continuar...");
    getchar();
}

// Código Principal
int main() {
    setlocale(LC_ALL, "Portuguese");

    int opcao;
    do {
        opcao = menu();
        switch (opcao) {
            case 1:
                cadastramentoAluno();
                break;
            case 2:
                listarAlunos();
                break;
            case 3:
                lancarNota();
                break;
            case 4:
                sair();
                break;
            default:
                erro();
                break;
        }
    } while (opcao != 4);

    return 0;
}
