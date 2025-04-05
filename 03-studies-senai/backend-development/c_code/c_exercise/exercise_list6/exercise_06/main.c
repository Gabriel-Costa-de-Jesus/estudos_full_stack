// Inclusão de Bibliotecas
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>
#include <unistd.h> 

// definição de tamanho
#define MAX_SIZE 5

struct System{
    char nome[50], sexo;
    int idade;
    float altura;
}; struct System sistema[MAX_SIZE];

// Variáveis Globais
int contador = 0;

// Protótipo de Função
void pressAnyKey();

// Funções do código
int menu() {
    int opcao;
    printf("\nEscolha uma opção abaixo:");
    printf("\n1- Cadastrar");
    printf("\n2- Exibir");
    printf("\n3- Sair do Sistema");
    printf("\nEscolha a sua Opção: ");
    scanf("%d", &opcao);
    while (getchar() != '\n'); // Limpar buffer do teclado
    return opcao;
}
void cadastrar() {
    if (contador >= MAX_SIZE){ printf("\nLimite Atinjido!"); return;}

    for (int i =0; i < MAX_SIZE; i++) {
        printf("\nDigite o nome da pessoa [%d]: ", i + 1);
        fgets(sistema[contador].nome, 50, stdin);
        sistema[contador].nome[strcspn(sistema[contador].nome, "\n")] = '\0';

        printf("\nDigite o sexo: ");
        scanf("%c", &sistema[contador].sexo);

        printf("\nDigite o idade da pessoa: ");
        scanf("%d", &sistema[contador].idade);

        printf("\nDigite a altura da pessoa: ");
        scanf("%f", &sistema[contador].altura);
    
        while (getchar() != '\n');
        contador++;
        
    }
    printf("\nCadastrado feito com Sucesso!");
}

void exibir() {
    if(contador == 0){printf("\nCadastre Primeiro!"); return;}

    printf("\nItens Cadastrados no Sistema:\n ");
    for (int i =0; i < MAX_SIZE; i++) {
        printf("\nNome da pessoa: %s", sistema[i].nome);
        printf("\nSexo: %c", sistema[i].sexo);
        printf("\nIdade: %d", sistema[i].idade);
        printf("\nAltura: %.2f", sistema[i].altura);
        printf("\n");
    }
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

// Funções Auxiliáres
void erro() {
    printf("\nOpção inválida, tente novamente!\n");
}

void pressAnyKey() {
    printf("\nPressione Enter para continuar...");
    getchar();
}
void delay() {
    sleep(2);
    system("cls");
}
// Função Principal
int main() {
    setlocale(LC_ALL, "Portuguese");

    int opcao;
    do {
        opcao = menu();
        switch (opcao) {
            case 1:
                cadastrar();
                break;
            case 2:
                exibir();
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

