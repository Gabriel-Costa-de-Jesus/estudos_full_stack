#include <stdio.h>
#include <locale.h>
#include <string.h> //Biblioteca para conversão de tipo de dado
#include <stdlib.h> // Biblioteca do CLS
#include <unistd.h> // Biblioteca do Sleep

struct DadosAlunos {
    char nome[50];  
    float altura;
    int idade;
}; struct DadosAlunos alunos[100];

int contador = 0;

void replace(char *txt); // Declarando a existência da função, pq se não, a função replace ela é chamada antes de ela de fato aparecer no código, pois no código eu tou chamando ela primeiro e dps declarando, para não dar erro adiciono está linha.

int menu() {
    int opcao;
    printf("\nEscolha uma opção Abaixo: ");
    printf("\n1 - Cadastrar Aluno ");
    printf("\n2 - Exibir alunos Cadastrados ");
    printf("\n3 - Limpar Tela ");
    printf("\n4 - Sair do Sistema\n");
    printf("Digite a sua opção: ");
    scanf("%d", &opcao);
    return opcao;
}

void cadastrarAlunos() {
    if (contador >= 100) {  
        printf("\nLimite de alunos atingido!\n");
        return;
    }
    
    char inputReplace[50];

  	fflush(stdin); // Se tiver comendo Enter, é só usar antes de ler 
  
    printf("\nDigite o nome do aluno: ");
    fgets(alunos[contador].nome, 50, stdin); // Ou posso usar o gets(alunos[contador].nome); não recomendado

    printf("\nDigite a altura do aluno: ");
    scanf("%s", inputReplace); // Recebe o dado em String
    replace(inputReplace); // Envia o dado para fazer a troca
    alunos[contador].altura = strtof(inputReplace, NULL); // Armazena no struct e converte de char para float

    printf("\nDigite a idade do aluno: ");
    scanf("%d", &alunos[contador].idade);

    printf("\nAluno: %s Cadastrado com sucesso!\n", alunos[contador].nome);
    
    contador++; 
}
void exibirAlunos() {
    if (contador == 0) {
        printf("\nCadastre algum aluno primeiro! \n");
    } else {
        printf("Alunos Cadastrados no Sistema: \n");
        for (int i = 0; i < contador; i++) {
            printf("\nNome do aluno: %s", alunos[i].nome);
            printf("\nAltura do aluno: %.2f", alunos[i].altura);
            printf("\nIdade do aluno: %d\n", alunos[i].idade);
        }
    }    
}

void replace(char * txt){ // Recebe o texto em char
    for (int i = 0; txt[i] != '\0'; i++) { // Vasculha toda string, '\0' Significa para ir até o final
        if (txt[i] == '.') { // Procura . na string
            txt[i] = ','; // Substitui por ,
        }
    }
}

void sair() {
    printf("Saindo do sistema...\n");
}

void erro() {
    printf("Opção Inválida! Tente Novamente! \n");
}

void clearDelay(){
    printf("Limpando a Tela");
    for (int i = 0; i < 5; i++) {
        printf(".");
        sleep(1);
    }
    printf("\nSistema Limpo! Agradecemos pela a sua Paciência...");
    sleep(3);
    system("cls");
}

int main() {
    setlocale(LC_ALL, "Portuguese"); 

    printf("Seja Bem-vindo ao sistema de Alunos: \n");

    int opcao;

    do {
        opcao = menu();

        switch (opcao) {
            case 1:
                cadastrarAlunos();
                break;
            case 2:
                exibirAlunos();
                break;
            case 3:
                clearDelay();
                break;
            case 4:
                sair();
                break;
            default:
                erro();
        }
    } while (opcao != 4);

    return 0;
}