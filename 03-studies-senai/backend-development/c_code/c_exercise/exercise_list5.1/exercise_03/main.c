#include <stdio.h>
#include <locale.h>

int data(int dia, int mes, int ano, int dia2, int mes2, int ano2) {
    int dias;
    
    dias = (ano2 - ano) * 365 + (mes2 - mes) * 30 + (dia2 - dia); 
    printf("A pessoa viveu aproximadamente %d dias.\n", dias);
}

int main() {
    setlocale(LC_ALL, "Portuguese");

    int dia, mes, ano;

    printf("Digite o dia, o mês e o ano do seu nascimento (DDMMYYYY): ");
    scanf("%2d%2d%4d", &dia, &mes, &ano); 

    printf("Data de nascimento: %02d/%02d/%04d\n", dia, mes, ano);

    int dia2, mes2, ano2;

    printf("Digite o dia, o mês e o ano atual (DDMMYYYY): ");
    scanf("%2d%2d%4d", &dia2, &mes2, &ano2);  

    printf("Data atual: %02d/%02d/%04d\n", dia2, mes2, ano2);

    data(dia, mes, ano, dia2, mes2, ano2);

    return 0;
}
