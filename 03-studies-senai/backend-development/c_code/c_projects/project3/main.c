#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>  
#include <windows.h> 
#include <unistd.h>

#define MAX_SYSTEM 6

// Funções de Protótipos
void pressAnyKey();
void menu(int *option);
void canditado1(int *votos);
void canditado2(int *votos);
void canditado3(int *votos);
void canditado4(int *votos);
void nulo(int *votos);
void branco(int *votos);
void exibir(int *votos);
void sair();
void clearDelay();
void erro();

int contador = 0;

void menu(int *option) {
    printf("\nEscolha um canditado Abaixo: ");
    printf("\n1 - Pablo Marçal");
    printf("\n2 - Prefeito de Sorocaba");
    printf("\n3 - Lula");
    printf("\n4 - Bolsonaro");
    printf("\n5 - Nulo");
    printf("\n6 - Branco");
    printf("\n7 - Exibir Votos");
    printf("\n8 - Sair do Sistema");
    printf("\nDigite a sua opção: ");
    scanf("%d", option);
    while (getchar() != '\n');
}

void canditado1(int *votos) { 
    votos[0]++;
    contador++;
    printf("\nVoto registrado para Pablo Marçal!\n");
}

void canditado2(int *votos) { 
    votos[1]++;
    contador++;
    printf("\nVoto registrado para Prefeito de Sorocaba!\n");
}

void canditado3(int *votos) { 
    votos[2]++;
    contador++;
    printf("\nVoto registrado para Lula!\n");
}

void canditado4(int *votos) { 
    votos[3]++;
    contador++;
    printf("\nVoto registrado para Bolsonaro!\n");
}

void nulo(int *votos) {
    votos[4]++;
    contador++;
    printf("\nVoto registrado como Nulo!\n");
}

void branco(int *votos) {
    votos[5]++;
    contador++;
    printf("\nVoto registrado como Branco!\n");
}

void exibir(int *votos) {
    if (contador == 0) {
        printf("\nNenhuma pessoa votou ainda!\n");
        return;
    }
    printf("\n--- Resultados de Votação ---\n");
    printf("Pablo Marçal: %d votos\n", votos[0]);
    printf("Prefeito de Sorocaba: %d votos\n", votos[1]);
    printf("Lula: %d votos\n", votos[2]);
    printf("Bolsonaro: %d votos\n", votos[3]);
    printf("Nulo: %d votos\n", votos[4]);
    printf("Branco: %d votos\n", votos[5]);
    pressAnyKey();
}

void sair() {
    printf("\nSaindo do Sistema");
    for (int i = 0; i < 5; i++) {
        printf(".");
        sleep(1);
    }
    printf("\nAgradecemos por utilizar nosso Sistema!\n");
    sleep(2);
}

void clearDelay() {
    sleep(2);
    system("cls");  
}

void pressAnyKey() {
    printf("\n");
    system("pause");
}

void erro() {
    printf("\nOpção inválida! Tente novamente!\n");
}

int main() {
    setlocale(LC_ALL, "Portuguese");
    int option;

    // Alocação dinâmica para os votos Mallocão
    int *votos = (int *)calloc(MAX_SYSTEM, sizeof(int));
    
    if (votos == NULL) {
        printf("\nErro ao alocar memória.\n");
        return 1;
    }

    do {
        menu(&option);

        switch (option) {
            case 1:
                canditado1(votos);
                break;
            case 2:
                canditado2(votos);
                break;
            case 3:
                canditado3(votos);
                break;
            case 4:
                canditado4(votos);
                break;
            case 5:
                nulo(votos);
                break;
            case 6:
                branco(votos);
                break;
            case 7:
                exibir(votos);
                break;
            case 8:
                sair();
                break;
            default:
                erro();
                break;
        }

        clearDelay();
    } while (option != 8);

    
    free(votos); // Estou fazendo uma tLiberação de memória alocada
    return 0;
}
