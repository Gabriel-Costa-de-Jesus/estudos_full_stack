#include <stdio.h>
#include <locale.h>

#define MAX_SYSTEM 3

struct Estudante {
    char nome[50];
    int matricula;
    float nota1, nota2, nota3, media;
}; struct Estudante estudante[MAX_SYSTEM];

int contador = 0, maiorNota = 0, menorNota=9999, indiceMaior =0 , indiceMenor = 0;
int menu(){
    int opcao;
    printf("\n1- Cadastrar estudante");
    printf("\n2- Exibir média dos estudantes");
    printf("\n3- Exibir classificação dos estudantes");
    printf("\n4- Relatório final");
    printf("\n5 - Sair");
    printf("\nEscolha a sua opção: ");
    scanf("%d", &opcao);
    fflush(stdin);
    return opcao;
}
void cadastro(){
    printf("\nDigite o nome do estudante! ");
    fgets(estudante[contador].nome, 50, stdin);

    printf("\nDigite o código de Matricula: ");
    scanf("%d", &estudante[contador].matricula);

    printf("\nDigite a nota da primeira Unidade: ");
    scanf("%f", &estudante[contador].nota1);

    printf("\nDigite a nota da segunda Unidade: ");
    scanf("%f", &estudante[contador].nota2);

    printf("\nDigite a nota da terceira Unidade: ");
    scanf("%f", &estudante[contador].nota3);

    printf("\nEstudante Cadastrado");
    contador++;

}
void exibirMedia(){
    for (int i =0; i < contador; i++) {
        estudante[i].media = (estudante[i].nota1+estudante[i].nota2+estudante[i].nota3)/3;
    }

    for (int i =0; i < contador; i++) {
      printf("\nEstudante: %s", estudante[i].nome);
     printf("\nMedia: %f", estudante[i].media);
    }
    
}
void exibirClassificacao() {
    for (int i =0; i < contador; i++) {
        if (estudante[i].media > maiorNota) {
        maiorNota= estudante[i].media;
        indiceMaior=i;
        }
        if(estudante[i].media < menorNota) {
            menorNota = estudante[i].media;
            indiceMenor=i;
        }

    }
    
    
}
void relatorioFinal() {
    printf("\nEstudante com a maior Nota: %s", estudante[indiceMaior].nome);
    printf("\nMédia do estudante: %d", maiorNota);


    printf("\nEstudante com a menor Nota: %s", estudante[indiceMenor].nome);
     printf("\nMédia do estudante: %d", menorNota);
}
void sair() {
    printf("\nSaindo do Sistema");
}
void erro(){
    printf("\nOpção Inválida! Tente Novamente");
}
int main(){
    setlocale(LC_ALL, "Portuguese");

    int opcao;

    do{
        opcao = menu();

        switch(opcao){
            case 1:
            cadastro();
            break;
            case 2:
            exibirMedia();
            break;
            case 3:
            exibirClassificacao();
            break;
            case 4:
            relatorioFinal();
            break;
            case 5:
            sair();
            default:
            erro();
            break;
        }
    } while (opcao != 5);
}