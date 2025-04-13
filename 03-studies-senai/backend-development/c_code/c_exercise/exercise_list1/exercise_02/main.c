// Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância Total percorrida pelo automóvel e o total de combustível gasto.
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    int n1,n2;

    printf("\nDigite a distancia pecorrida em km: ");
    scanf("%d", &n1);

    printf("\nDigite a quantidade de litros gasto: ");
    scanf("%d", &n2);

    printf("\nConsumo médio de gasolina: %d Km/L", n1/n2);

}
