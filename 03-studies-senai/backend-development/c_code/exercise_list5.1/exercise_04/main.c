#include <stdio.h>
#include <locale.h>

int verificador(int num) {
    return num > 0; // Uma pequena condi��o para verificar se um n�mero �  V ou F
}

int main() {
    setlocale(LC_ALL, "Portuguese");

    int num;

    printf("Digite um n�mero: ");
    scanf("%d", &num); 

    if (verificador(num)) { // Essa fun��o s� ir� ser executada se for True, como se fosse um IF Not em python
        printf("Este n�mero � Verdadeiro: %d", num);
    }
    else {
        printf("Este n�mero � falso: %d", num);
    }
    
    return 0;
}
