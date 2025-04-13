// Faça algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês.
// — Considere fixo o juro da poupança em 0,70% a. m.
#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    float n1;

    printf("\nDigite o valor depositado: ");
    scanf("%f", &n1);

    printf("\nRendimento foi de %.2f e o redimento total foi: %.2f", n1*0.007, (n1*0.007) + n1);
}
