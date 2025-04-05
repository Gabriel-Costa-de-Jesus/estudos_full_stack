// Inclus�o de Bibliotecas
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>
#include <unistd.h> 

// defini��o de tamanho
#define MAX_SIZE 5

struct System{
    char descricao[50];
    int codigo, quantidade;
    float preco, totalProduto;
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
        printf("\nDigite a descricao do produto [%d]: ", i + 1);
        fgets(sistema[contador].descricao, 50, stdin);
        sistema[contador].descricao[strcspn(sistema[contador].descricao, "\n")] = '\0';

        printf("\nDigite o c�digo: ");
        scanf("%d", &sistema[contador].codigo);
       

        printf("\nDigite a quantidade do produto: ");
        scanf("%d", &sistema[contador].quantidade);

        printf("\nDigite o pre�o do produto: ");
        scanf("%f", &sistema[contador].preco);

        sistema[i].totalProduto = sistema[i].quantidade * sistema[i].preco;
    
        while (getchar() != '\n');
        contador++;
        
    }
    printf("\nCadastrado feito com Sucesso!");
}

void exibir() {
    if(contador == 0){printf("\nCadastre Primeiro!"); return;}

    printf("\nItens Cadastrados no Sistema:\n ");
    for (int i =0; i < MAX_SIZE; i++) {
        printf("\nNome da descricao do Produto: %s", sistema[i].descricao);
        printf("\nCodigo: %d", sistema[i].codigo);
        printf("\nQuantidade: %d", sistema[i].quantidade);
        printf("\nPre�o Unit�rio: R$ %.2f", sistema[i].preco);
        printf("\nPre�o Total: R$ %.2f", sistema[i].totalProduto);
        printf("\n");
       
    }
    

    printf("\nO pre�o total de cada produtos s�o: ");
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

