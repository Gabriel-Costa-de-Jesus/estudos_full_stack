#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int num[8], guardar_maior, guardar_menor, posicao_maior, posicao_menor;

    printf("Digite 8 números:\n");

    for (int contador = 0; contador < 8; contador++) {
        printf("Número[%d]: ", contador + 1);
        scanf("%d", &num[contador]);
    }

    // Inicializar maior e menor com o primeiro elemento do vetor
    guardar_maior = num[0];
    guardar_menor = num[0];
    posicao_maior = 0;
    posicao_menor = 0;

    // Exibir os números digitados
    printf("\nOs números digitados foram:\n");
    for (int contador = 0; contador < 8; contador++) {
        printf("%d ", num[contador]);

        // Verificar o maior número
        if (num[contador] > guardar_maior) {
            guardar_maior = num[contador];
            posicao_maior = contador;
        }

        // Verificar o menor número
        if (num[contador] < guardar_menor) {
            guardar_menor = num[contador];
            posicao_menor = contador;
        }
    }

    // Exibir o maior e o menor número com suas posições
    printf("\n\nO maior número foi: %d", guardar_maior);
    printf("\nA sua posição no vetor é: %d", posicao_maior);

    printf("\n\nO menor número foi: %d", guardar_menor);
    printf("\nA sua posição no vetor é: %d", posicao_menor);
}