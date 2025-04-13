#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    int n1, n2;
    printf("Digite o primeiro número: ");
    scanf("%d", &n1);

    printf("Digite o segundo número: ");
    scanf("%d", &n2);

    printf("A soma de %d e %d é: %d", n1, n2, n1+n2);

}

//Faça um algoritmo que receba dois números e exiba o resultado da uma soma.

