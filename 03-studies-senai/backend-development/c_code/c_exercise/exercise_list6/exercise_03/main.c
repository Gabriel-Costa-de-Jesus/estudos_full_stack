// Inclus�o de Bibliotecas
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>
#include <unistd.h> 

// defini��o de tamanho
#define MAX_SIZE 10

struct System{
    char titulo[50], autor[50];
    int ano_publicacao;
    float preco;
}; struct System sistema[MAX_SIZE];

// Vari�veis Globais
int contador = 0;

// Prot�tipo de Fun��o
void pressAnyKey();

// Fun��es do c�digo
int menu() {
    int opcao;
    printf("\nEscolha uma op��o abaixo:");
    printf("\n1- Cadastrar");
    printf("\n2- Exibir");
    printf("\n3- Sair do Sistema");
    printf("\nEscolha a sua Op��o: ");
    scanf("%d", &opcao);
    while (getchar() != '\n'); // Limpar buffer do teclado
    return opcao;
}
void cadastrar() {
    if (contador >= MAX_SIZE){ printf("\nLimite Atinjido!"); return;}

    for (int i =0; i < MAX_SIZE; i++) {
        printf("\nDigite o t�tulo do livro [%d]: ", i + 1);
        fgets(sistema[contador].titulo, 50, stdin);
        sistema[contador].titulo[strcspn(sistema[contador].titulo, "\n")] = '\0';

        printf("\nDigite o nome do autor: ");
        fgets(sistema[contador].autor, 50, stdin);
        sistema[contador].autor[strcspn(sistema[contador].autor, "\n")] = '\0';

        printf("\nDigite o ano de publica��o: ");
        scanf("%d", &sistema[contador].ano_publicacao);

        printf("\nDigite o pre�o do livro: ");
        scanf("%f", &sistema[contador].preco);
    
        while (getchar() != '\n');
        contador++;
        
    }
    printf("\nCadastrado feito com Sucesso!");
}

void exibir() {
    if(contador == 0){printf("\nCadastre Primeiro"); return;}

    printf("\nItens Cadastrados no Sistema:\n ");
    for (int i =0; i < MAX_SIZE; i++) {
        printf("\nT�tulo: %s", sistema[i].titulo);
        printf("\nAutor: %s", sistema[i].autor);
        printf("\nAno da Publica��o: %d", sistema[i].ano_publicacao);
        printf("\nPreco: R$ %.2f", sistema[i].preco);
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

