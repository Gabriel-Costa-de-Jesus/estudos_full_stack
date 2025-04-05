// Inclus�o de Bibliotecas
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>
#include <unistd.h> 

// defini��o de tamanho
#define MAX_FUNCIONARIOS 5

struct SystemEmpresarial{
    char nome[50], cargo[50];
    int idade;
    float salario;
}; struct SystemEmpresarial sistema[MAX_FUNCIONARIOS];

// Vari�veis Globais
int contador = 0;

// Prot�tipo de Fun��o
void pressAnyKey();

// Fun��es do c�digo
int menu() {
    int opcao;
    printf("\nEscolha uma op��o abaixo:");
    printf("\n1- Cadastrar Funcion�rio");
    printf("\n2- Calcular Sal�rio");
    printf("\n3- Sair do Sistema");
    printf("\nEscolha a sua Op��o: ");
    scanf("%d", &opcao);
    while (getchar() != '\n'); // Limpar buffer do teclado
    return opcao;
}
void cadastroFuncionarios() {
    if (contador >= MAX_FUNCIONARIOS){ printf("\nLimite Atinjido!"); return;}

    for (int i =0; i < MAX_FUNCIONARIOS; i++) {
        printf("\nDigite o nome do Funcion�rio [%d]: ", i + 1);
        fgets(sistema[contador].nome, 50, stdin);
        sistema[contador].nome[strcspn(sistema[contador].nome, "\n")] = '\0';

        printf("\nDigite seu cargo: ");
        fgets(sistema[contador].cargo, 50, stdin);
        sistema[contador].cargo[strcspn(sistema[contador].cargo, "\n")] = '\0';

        printf("\nDigite seu sal�rio: ");
        scanf("%f", &sistema[contador].salario);

        printf("\nDigite a sua idade: ");
        scanf("%d", &sistema[contador].idade);
    
        while (getchar() != '\n');
        contador++;
        
    }
    printf("\nFuncion�rios Cadastrados com Sucesso!");
}

void calcularSalario() {
    if(contador == 0){printf("\nCadastre um funcion�rio primeiro"); return;}

    float soma =0, mediaSalarial =0;
    printf("\nFuncion�rios Cadastrados no Sistema:\n ");
    for (int i =0; i < MAX_FUNCIONARIOS; i++) {
        printf("\nFuncion�rio: %s", sistema[i].nome);
        printf("\nCargo: %s", sistema[i].cargo);
        printf("\nSal�rio: R$ %.2f", sistema[i].salario);
        printf("\nIdade: %d anos", sistema[i].idade);
        printf("\n");

        soma += sistema[i].salario;
    }
    mediaSalarial = soma/MAX_FUNCIONARIOS;

    printf("\nA m�dia salarial dos funcion�rios: R$ %.2f", mediaSalarial);

    pressAnyKey();
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

// Fun��es Auxili�res
void erro() {
    printf("\nOp��o inv�lida, tente novamente!\n");
}

void pressAnyKey() {
    printf("\nPressione Enter para continuar...");
    getchar();
}
void delay() {
    sleep(2);
    system("cls");
}
// Fun��o Principal
int main() {
    setlocale(LC_ALL, "Portuguese");

    int opcao;
    do {
        opcao = menu();
        switch (opcao) {
            case 1:
                cadastroFuncionarios();
                break;
            case 2:
                calcularSalario();
                break;
            case 3:
                sair();
                break;
            default:
                erro();
                break;
        }
        delay();
    } while (opcao != 3);

    return 0;
}

