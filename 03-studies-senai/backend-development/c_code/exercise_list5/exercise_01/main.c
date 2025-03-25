#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int num[8], guardar_maior, guardar_menor, posicao_maior, posicao_menor;

    printf("Digite 8 n�meros:\n");

    for (int contador = 0; contador < 8; contador++) {
        printf("N�mero[%d]: ", contador + 1);
        scanf("%d", &num[contador]);
    }

    // Inicializar maior e menor com o primeiro elemento do vetor
    guardar_maior = num[0];
    guardar_menor = num[0];
    posicao_maior = 0;
    posicao_menor = 0;

    // Exibir os n�meros digitados
    printf("\nOs n�meros digitados foram:\n");
    for (int contador = 0; contador < 8; contador++) {
        printf("%d ", num[contador]);

        // Verificar o maior n�mero
        if (num[contador] > guardar_maior) {
            guardar_maior = num[contador];
            posicao_maior = contador;
        }

        // Verificar o menor n�mero
        if (num[contador] < guardar_menor) {
            guardar_menor = num[contador];
            posicao_menor = contador;
        }
    }

    // Exibir o maior e o menor n�mero com suas posi��es
    printf("\n\nO maior n�mero foi: %d", guardar_maior);
    printf("\nA sua posi��o no vetor �: %d", posicao_maior);

    printf("\n\nO menor n�mero foi: %d", guardar_menor);
    printf("\nA sua posi��o no vetor �: %d", posicao_menor);
}