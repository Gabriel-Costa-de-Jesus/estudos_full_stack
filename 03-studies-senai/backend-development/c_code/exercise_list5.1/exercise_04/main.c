#include <stdio.h>
#include <locale.h>

int verificador(int num) {
    return num > 0; // Uma pequena condição para verificar se um número é  V ou F
}

int main() {
    setlocale(LC_ALL, "Portuguese");

    int num;

    printf("Digite um número: ");
    scanf("%d", &num); 

    if (verificador(num)) { // Essa função só irá ser executada se for True, como se fosse um IF Not em python
        printf("Este número é Verdadeiro: %d", num);
    }
    else {
        printf("Este número é falso: %d", num);
    }
    
    return 0;
}
