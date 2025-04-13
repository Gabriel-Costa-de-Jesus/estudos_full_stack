// AFaça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo recebera um acréscimo de acordo com um percentual informado pelo usuário.
#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    float custo, margem;

    printf("\nDigite o preço do produto: ");
    scanf("%f", &custo);

    printf("\nDigite a porcentagem que deseja lucrar: ");
    scanf("%f", &margem);

    printf("\nLucro: %.2f \nLucro Total: %.2f", custo*(margem/100), custo*(margem/100) + custo );
}