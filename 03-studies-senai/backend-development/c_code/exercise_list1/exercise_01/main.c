#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {

    setlocale(LC_ALL, "Portuguese");
    
    int a,b,c;

    printf("Digite um n�mero: ");
    scanf("%d", &a);

    printf("Digite outro n�mero: ");
    scanf("%d", &b);

    printf("Digite mais um n�mero: ");
    scanf("%d", &c);

    if(a + b > c) {
        printf("A soma de A + B � maior que C");
    }
    else{
        printf("A soma de A + B � menor que C");
    }

}