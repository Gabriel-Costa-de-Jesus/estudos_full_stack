# include <stdio.h>
# include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int number[10], soma = 0;

    printf("Digite 10 números Inteiros: \n");
    for(int count = 0; count < 10; count++) {
        printf("Número[%d]: ", count +1);
        scanf("%d", &number[count]);

        soma = number[count] + soma;

    } printf("A soma de todos os números digitados é: %d", soma);
}