#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <locale.h>

#define MAX_SYSTEM 500

// Definindo Struct
struct Data {
    int dia, mes, ano;
}; 

// Protótipos
void pressAnyKey();
void compararDatas(struct Data d1, struct Data d2);

// Menu
int menu() {
    int option;
    printf("\nEscolha uma opção abaixo: ");
    printf("\n1 - Ver qual data aconteceu primeiro");
    printf("\n2 - Sair do Sistema");
    printf("\nEscolha uma opção: ");
    scanf("%d", &option);
    while (getchar() != '\n');
    return option;
}

// Registro de datas e comparação
void registrationdata() {
    struct Data d1, d2;

    printf("\n--- Primeira Data ---");
    printf("\nDigite o dia: ");
    scanf("%d", &d1.dia);
    printf("Digite o mês: ");
    scanf("%d", &d1.mes);
    printf("Digite o ano: ");
    scanf("%d", &d1.ano);

    printf("\n--- Segunda Data ---");
    printf("\nDigite o dia: ");
    scanf("%d", &d2.dia);
    printf("Digite o mês: ");
    scanf("%d", &d2.mes);
    printf("Digite o ano: ");
    scanf("%d", &d2.ano);

    compararDatas(d1, d2);
    pressAnyKey();
}

void compararDatas(struct Data d1, struct Data d2) {
    if (d1.ano < d2.ano) {
        printf("\nA primeira data ocorreu primeiro.");
    } else if (d1.ano > d2.ano) {
        printf("\nA segunda data ocorreu primeiro.");
    } else {
        // Ano igual
        if (d1.mes < d2.mes) {
            printf("\nA primeira data ocorreu primeiro.");
        } else if (d1.mes > d2.mes) {
            printf("\nA segunda data ocorreu primeiro.");
        } else {
            // Mês igual
            if (d1.dia < d2.dia) {
                printf("\nA primeira data ocorreu primeiro.");
            } else if (d1.dia > d2.dia) {
                printf("\nA segunda data ocorreu primeiro.");
            } else {
                printf("\nAs datas são iguais.");
            }
        }
    }
}

// Encerramento
void exitt() {
    printf("\nSaindo do Sistema");
    for (int i = 0; i < 5; i++) {
        printf(".");
        sleep(1);
    }
    printf("\nAgradecemos por utilizar nosso Sistema!");
    sleep(2);
}

// Utilitários
void clearDelay() {
    sleep(2);
    system("cls");
}

void pressAnyKey() {
    printf("\n\n");
    system("pause");
}

void error() {
    printf("\nOpção inválida! Tente novamente!");
}

// Main
int main() {
    setlocale(LC_ALL, "Portuguese");

    int option;
    do {
        option = menu();
        switch (option) {
            case 1:
                registrationdata();
                break;
            case 2:
                exitt();
                break;
            default:
                error();
                break;
        }
        clearDelay();
    } while (option != 2);

    return 0;
}
