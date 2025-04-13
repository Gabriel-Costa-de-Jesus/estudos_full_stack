// Bibliotecas Necessárias
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <locale.h>

// Definindo tamanho de Sistema
#define MAX_SYSTEM 500

// Definindo Struct
struct Pessoa {
    char nome[50];
    int idade;
    float altura;
}; struct Pessoa pessoa[MAX_SYSTEM];

// Variávies Globais
int countPeople = 0;

// Protótipos de Funções
void pressAnyKey();

// Funções principais
int menu(){
	int option;
	printf("\nEscolha uma opção abaixo: ");
	printf("\n1 - Cadastrar Pessoa");
	printf("\n2 - Listar Pessoas cadastradas");
	printf("\n3 - Sair do Sistema");
	printf("\nEscolha uma opção: ");
	scanf("%d", &option);
	while (getchar() != '\n');
	return option;
}

void registrationPeople() {
    if (countPeople >= MAX_SYSTEM) {
        printf("\nLimite Atinjido!");
        return;
    }

    printf("\nDigite seu nome(a): ");
    fgets(pessoa[countPeople].nome, 50, stdin);
    pessoa[countPeople].nome[strcspn(pessoa[countPeople].nome, "\n")] = '\0';

    printf("\nDigite a sua idade: ");
    scanf("%d", &pessoa[countPeople].idade);

    printf("\nDigite a sua altura: ");
    scanf("%f", &pessoa[countPeople].altura);

    printf("\nPessoa Cadastrada com Sucesso!");

    countPeople++;

}
void userList(){
	if (countPeople == 0){
		printf("\nCadastre alguma pessoa primeiro! ");
	    return;
	}
	printf("\nUsuários Cadastrados!\n");
	for (int i =0; i < countPeople; i++) {
		printf("\nNome: %s", pessoa[i].nome);
		printf("\nIdade: %d anos", pessoa[i].idade);
		printf("\nAltura: %.2f", pessoa[i].altura);
		printf("\n");
	}
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
// Funções Auxiliáres
void clearDelay() {
	sleep(2);
	system("cls");
}

void pressAnyKey() {
	printf("\n\n");
	system("pause");
}

void error(){
	printf("\nOpção inválida! Tente novamente!");
}
// Função Principal
int main() {
	setlocale(LC_ALL, "Portuguese");
	
	int option;
	do{
		option = menu();
		switch (option) {
			   	case 1:
				   registrationPeople();
				   break;
				case 2:
					 userList();
					 break;
				case 3:
					 exitt();
					 break;
				default:
					  error();
					  break;  
	    }
    	clearDelay();
	} while(option != 3);

	return 0;
}
