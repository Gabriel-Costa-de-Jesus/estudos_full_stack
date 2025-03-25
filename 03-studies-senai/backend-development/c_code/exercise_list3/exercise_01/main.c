#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {

    setlocale(LC_ALL, "Portuguese");
    
    int a,b,c;

    printf("Digite um número: ");
    scanf("%d", &a);

    printf("Digite outro número: ");
    scanf("%d", &b);

    printf("Digite mais um número: ");
    scanf("%d", &c);

    if(a + b > c) {
        printf("A soma de A + B é maior que C");
    }
    else{
        printf("A soma de A + B é menor que C");
    }

}