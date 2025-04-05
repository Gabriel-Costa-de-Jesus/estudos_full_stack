// Inclusão de Bibliotecas
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>
#include <unistd.h> 

// definição de tamanho
#define MAX_SIZE 3

struct System{
    char marca[50], modelo[50]; 
    int ano; 
    float preco;
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
        printf("\nDigite o nome da marca [%d]: ", i + 1);
        fgets(sistema[contador].marca, 50, stdin);
        sistema[contador].marca[strcspn(sistema[contador].marca, "\n")] = '\0';

        printf("\nDigite o modelo: ");
        fgets(sistema[contador].modelo, 50, stdin);
        sistema[contador].modelo[strcspn(sistema[contador].modelo, "\n")] = '\0';

        printf("\nDigite o ano do carro: ");
        scanf("%d", &sistema[contador].ano);

        printf("\nDigite o preço do carro: ");
        scanf("%f", &sistema[contador].preco);
    
        while (getchar() != '\n');
        contador++;
        
    }
    printf("\nCadastrado feito com Sucesso!");
}

void exibir() {
    if(contador == 0){printf("\nCadastre Primeiro!"); return;}

    printf("\nItens Cadastrados no Sistema:\n ");
    for (int i =0; i < MAX_SIZE; i++) {
        printf("\nNome da Marca: %s", sistema[i].marca);
        printf("\nModelo: %s", sistema[i].modelo);
        printf("\nAno: %d", sistema[i].ano);
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

