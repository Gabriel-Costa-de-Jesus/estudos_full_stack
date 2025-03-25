#include <stdio.h>
#include <locale.h>

int soma(int num, int somar) {
    somar += num; 
    return somar;
}

int main() {
    setlocale(LC_ALL, "Portuguese");

    int num, somar = 0; 
    printf("Digite um número, digite 0 para sair\n");

    do {
        printf("Digite um número: ");
        scanf("%d", &num);

        if (num != 0) {
            somar = soma(num, somar); 
        }

    } while (num != 0); 

    printf("A soma de todos os números é: %d\n", somar);

    return 0;
}