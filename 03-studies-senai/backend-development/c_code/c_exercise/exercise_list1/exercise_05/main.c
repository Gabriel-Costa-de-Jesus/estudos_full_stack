// A Loja Mamão com Açucar está vendendo seus produtos em 5 (cinco) prestações sem juros.
// Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.
#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    float n1;

    printf("\nDigite o valor da compra: ");
    scanf("%f", &n1);

    printf("\nPrestações: R$%.2f sem juros", n1/5);
}