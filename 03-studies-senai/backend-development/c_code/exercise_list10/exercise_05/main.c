# include <stdio.h>
# include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int number[5], sum = 0, multiply = 1;

    printf("Digite 5 números Inteiros: \n");
    for(int count = 0; count < 5; count++) {
        printf("Número[%d]: ", count +1);
        scanf("%d", &number[count]);

        if (number[count] % 2 == 1) {
            sum = number[count] + sum;
        }
        if (number[count] % 2 == 0) {
            multiply = number[count] * multiply;
        }

    } 
    printf("\nA soma de todos os números digitados impares é: %d", sum);
    printf("\nA Multiplicação de todos os números digitados pares é: %d", multiply);
}