// Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int n1,n2, n3;
    char nome[50];

    printf("\nDigite o nome do aluno: ");
    scanf("%s", nome);

    printf("\nDigite a primeira nota: ");
    scanf("%d", &n1);

    printf("\nDigite a segunda nota: ");
    scanf("%d", &n2);

    printf("\nDigite a terceira nota: ");
    scanf("%d", &n3);

    printf("\nO aluno %s ficou com a média: %d", nome, (n1+n2+n3)/3);
    

}
