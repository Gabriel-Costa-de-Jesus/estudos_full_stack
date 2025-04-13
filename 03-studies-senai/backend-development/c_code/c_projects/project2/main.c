// Definição das Bibliotecas
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <locale.h>

// Definição de Tamanho
#define MAX_SYSTEM 500
#define MAX_NOTAS 3

struct Estudante {
	char nome[50], matricula[20];
	float notas[MAX_NOTAS], media;
}; struct Estudante estudante[MAX_SYSTEM];

// Variáveis Globais
int contador = 0, countMedia =0, contadorAprovado =0, contadorReprovado = 0;
int posicaoMaior =0, posicaoMenor =0;

// Protótipo de Função
void pressAnyKey();
// Funções Principais
int menu(){
	int opcao;
	printf("\nEscolha uma opção abaixo: ");
	printf("\n1 - Cadastrar estudante ");
	printf("\n2 - Exibir média dos estudantes ");
	printf("\n3 - Exibir classficação dos estudantes ");
	printf("\n4 - Relatório Final ");
	printf("\n5 - Sair do sistema ");
	printf("\nDigite a sua opção: ");
	scanf("%d", &opcao);
	while(getchar() != '\n');
	return opcao;
}

void cadastrarEstudante() {
	if (contador >= MAX_SYSTEM) {
		printf("\nLimite de Alunos Atinjidos!");
	    return;
	}
		printf("\nDigite o nome do aluno(a): ");
	    fgets(estudante[contador].nome, 50, stdin);
	    estudante[contador].nome[strcspn(estudante[contador].nome, "\n")] = '\0';
		    
		printf("\nDigite o código de matricula do aluno: ");
		scanf("%s", estudante[contador].matricula);
		
		for (int i =0; i < MAX_NOTAS; i++) {
			printf("\nDigite a nota[%d] do aluno: ", i+1);
	        scanf("%f", &estudante[contador].notas[i]);
		}	
		while(getchar() != '\n');
		contador++;												       
	
	printf("\nCadastrado Realizado com Sucesso!");
}

void calcularMedia(int i) {
	float alunosnotas = 0;
	for (int j =0; j < MAX_NOTAS; j++) {
        alunosnotas = alunosnotas + estudante[i].notas[j];
    } 
    estudante[i].media = alunosnotas/MAX_NOTAS;
} 


void exibirMedias() {
	if (contador == 0){
		printf("\nNenhum aluno Cadastrado no Sistema!");
	 	return;
	}
	
	
	for (int i =0; i < contador; i++) {
        calcularMedia(i);
		printf("\nAluno(a): %s", estudante[i].nome);
	    printf("\nMatrícula: %s", estudante[i].matricula);
    	for (int j =0; j < MAX_NOTAS; j++) {
	    	printf("\nNotas[%d]: %.2f", j+1, estudante[i].notas[j]);
  		}
       printf("\nMédia: %.2f", estudante[i].media);
       printf("\n");
	}
	pressAnyKey();
}

void classificarAprovacao() {
	if (contador == 0){
		printf("\nNenhum aluno Cadastrado no Sistema!");
	 	return;
	}
	
	contadorAprovado =0, contadorReprovado = 0; // Reinicio a contagem para evitar chamagem desnecessaria 
	for (int i = 0; i < contador; i++) {
        calcularMedia(i); // Caso a pessoa não tenha calculado antes
		printf("\n\nMédia do aluno(a) %s: %.2f", estudante[i].nome, estudante[i].media);
					 
			if(estudante[i].media >= 7){
				printf("\nAprovado!");
				contadorAprovado++;					  	
			} 
  			else if (estudante[i].media < 7) {
		  	    printf("\nReprovado!");
				contadorReprovado++;
			  }	
     }			
	pressAnyKey();
}

void gerarRelatorio(){
		if (contador == 0){
		printf("\nNenhum aluno Cadastrado no Sistema!");
	 	return;
	}

	for (int i =0; i < contador; i++) {
        calcularMedia(i); // Se a pessoa não tiver calculado a média antes
        if (estudante[i].media > estudante[posicaoMaior].media) { // Só atualiza se o número da posição 0 for maior que os outros números das outras posições, caso não seja, o maior número será o da posição 0
            posicaoMaior = i;
        }
        if (estudante[i].media < estudante[posicaoMenor].media) { // Só atualiza se o número da posição 0 for menor que os outros números das outras posições, caso não seja, o menor número será o da posição 0
            posicaoMenor =i;
        }			   		  	   					 	   
    }    
    classificarAprovacao();

	printf("\nQuantidade de alunos Aprovados: %d", contadorAprovado);
	printf("\nQuantidade de alunos Reprovados: %d", contadorReprovado);
	
	printf("\n\nAluno com a maior nota: %s", estudante[posicaoMaior].nome);
	printf("\nMédia: %.2f", estudante[posicaoMaior].media);
	
	printf("\n\nAluno com a menor nota: %s", estudante[posicaoMenor].nome);
	printf("\nMédia: %.2f", estudante[posicaoMenor].media);	
	
	pressAnyKey();
}

void sair() {
	printf("\nSaindo do Sistema");
	for (int i =0; i < 5; i++) {
		printf(".");
		sleep(1);
	}
}
// Funções Auxiliares
void pressAnyKey() {
	printf("\n\n");
	system("pause");
}
void erro() {
	printf("\nOpção Inváida! Tente Novamente!");
}
void clear(){
	sleep(2);
	system("cls");
}
int main() {
	setlocale(LC_ALL, "Portuguese");
	int opcao;
	do{
		opcao = menu();
			  
		switch (opcao) {
			case 1:
				   	cadastrarEstudante();
					break;
			case 2:
				    exibirMedias();
					break;	 
			case 3:						 									    	 
  	        	    classificarAprovacao();
  					break;        			      
			case 4:	
				 	gerarRelatorio();
		 			break;
			case 5: 
				 	sair();	
                    break;	 	   						  							 	 
			default:
					erro();	
                    break;													 
		}
     clear();
	} while (opcao != 5);
}