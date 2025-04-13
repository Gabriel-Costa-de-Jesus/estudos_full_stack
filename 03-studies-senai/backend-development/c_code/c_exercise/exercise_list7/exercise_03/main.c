// Bibliotecas Necess�rias
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <locale.h>

// Definindo tamanho de Sistema
#define MAX_SYSTEM 500

// Definindo Struct
struct Retangulo {
    float largura, altura;
}; struct Retangulo retangulo[MAX_SYSTEM];

// Vari�vies Globais
int countretangulo = 0;

// Prot�tipos de Fun��es
void pressAnyKey();

// Fun��es principais
int menu(){
	int option;
	printf("\nEscolha uma op��o abaixo: ");
	printf("\n1 - Calcular �rea do ret�ngulo");
	printf("\n2 - Sair do Sistema");
	printf("\nEscolha uma op��o: ");
	scanf("%d", &option);
	while (getchar() != '\n');
	return option;
}

void registrationRetangulo() {
    if (countretangulo >= MAX_SYSTEM) {
        printf("\nLimite Atinjido!");
        return;
    }
	float area;

    printf("\nDigite a largura do retangulo: ");
    scanf("%f", &retangulo[countretangulo].largura);

	printf("\nDigite a altura do retangulo: ");
    scanf("%f", &retangulo[countretangulo].altura);

	area = retangulo[countretangulo].altura * retangulo[countretangulo].largura;

	printf("\nA �rea do Rent�ngulo � de: %.2f", area);

    countretangulo++;
	pressAnyKey();
}

void exitt() {
	printf("\nSaindo do Sistema");
	for (int i =0; i < 5; i++) {
		printf(".");
		sleep(1);
	} printf("\nAgradecemos por utilizar nosso Sistema!");
      sleep(2);
}
// Fun��es Auxili�res
void clearDelay() {
	sleep(2);
	system("cls");
}

void pressAnyKey() {
	printf("\n\n");
	system("pause");
}

void error(){
	printf("\nOp��o inv�lida! Tente novamente!");
}
// Fun��o Principal
int main() {
	setlocale(LC_ALL, "Portuguese");
	
	int option;
	do{
		option = menu();
		switch (option) {
			   	case 1:
				   registrationRetangulo();
				   break;
				case 2:
					 exitt();
					 break;
				default:
					  error();
					  break;  
	    }
    	clearDelay();
	} while(option != 2);

	return 0;
}
