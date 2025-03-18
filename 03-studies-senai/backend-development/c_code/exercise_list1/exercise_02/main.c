#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

int main() {

    setlocale(LC_ALL, "Portuguese");

    char nome[30], sexo, EstadoCivil[15], tempo[10];

    printf("Qual seu nome? ");
    fgets(nome, sizeof(nome), stdin);
    nome[strcspn(nome, "\n")] = 0; // Remove o '\n' no final

    printf("Qual seu sexo? (M/F) ");
    scanf(" %c", &sexo); // Espaço antes do %c para evitar problemas com buffer

    printf("Qual seu estado civil? ");
    scanf("%s", EstadoCivil);

    if (sexo == 'F' && strcmp(EstadoCivil, "CASADA") == 0) {
        printf("Olá Casada!\n");

        printf("Quanto tempo de casada? ");
        scanf("%s", tempo);

        printf("Você está casada há %s anos.\n", tempo);
    }

    return 0;
}
