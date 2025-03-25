#include <stdio.h>
#include <locale.h>

void duracao(int horaI, int minutoI, int horaF, int minutoF) {
    int totalH, totalM;

    if (horaI < horaF) {
        totalH = horaF - horaI;
    } else {
        totalH = (horaF + 24) - horaI; 
    }

    if (minutoI < minutoF) {
        totalM = minutoF - minutoI;
    } else {
        totalM = (minutoF + 60) - minutoI; 
    }

    printf("A duração do jogo foi de %d horas e %d minutos\n", totalH, totalM);
}

int main() {
    setlocale(LC_ALL, "Portuguese");

    int horaI, horaF, minutoI, minutoF; 
    printf("Digite a hora de Início do jogo: ");
    scanf("%d", &horaI);

    printf("Digite o minuto de Início do jogo: ");
    scanf("%d", &minutoI);

    printf("Digite a hora de término do jogo: ");
    scanf("%d", &horaF);

    printf("Digite o minuto de término do jogo: ");
    scanf("%d", &minutoF);

    duracao(horaI, minutoI, horaF, minutoF);

    return 0;
}
