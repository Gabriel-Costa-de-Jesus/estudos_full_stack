// Faça um algoritmo que receba dois números e ao final mostre a soma, subtração, a multiplicação e a divisão dos números lidos.
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int n1,n2;

    printf("\nDigite um número: ");
    scanf("%d", &n1);

    printf("\nDigite outro número: ");
    scanf("%d", &n2);

    printf("\nA Soma de %d e %d é: %d", n1, n2, n1+n2);
    printf("\nA Subtração de %d e %d é: %d", n1, n2, n1-n2);
    printf("\nA Multiplicação de %d e %d é: %d", n1, n2, n1*n2);
    printf("\nA Divisão de %d e %d é: %d", n1, n2, n1/n2);

}
