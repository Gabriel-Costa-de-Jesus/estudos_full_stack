# include <stdio.h>
# include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int number[10], soma = 0;

    printf("Digite 10 n�meros Inteiros: \n");
    for(int count = 0; count < 10; count++) {
        printf("N�mero[%d]: ", count +1);
        scanf("%d", &number[count]);

        soma = number[count] + soma;

    } printf("A soma de todos os n�meros digitados �: %d", soma);
}