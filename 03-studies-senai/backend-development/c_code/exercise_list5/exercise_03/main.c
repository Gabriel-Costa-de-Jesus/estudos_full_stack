# include <stdio.h>
# include <locale.h>

int main() {

    setlocale(LC_ALL, "Portuguese");

    int number[10], divisorNumber;

    printf("Digite 10 números inteiros: \n");
    for(int count = 0; count < 10; count++) {
        printf("Número[%d]: ", count +1);
        scanf("%d", &number[count]);

        if (count == 9) {
            printf("Digite um número inteiro e positivo: ");
            scanf("%d", &divisorNumber);

            for(int count = 0; count < 10; count++) {
                if (number[count] % divisorNumber == 0) {
                    printf("Números que são divisíveis por %d: ", divisorNumber);
                    printf("%d", number[count]);
                    printf("\n");
                }
            }
        }
    }
}
