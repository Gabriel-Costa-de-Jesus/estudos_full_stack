# include <stdio.h>
# include <locale.h>


int par(){
    return printf("\nVerdadeiro");
}

int impar(){
    return printf("\nFalso");
}

int main(){

    setlocale(LC_ALL, "Portuguese");

    int n1;

    printf("Digite um n�mero: ");
    scanf("%d", &n1);

    if (n1 % 2 == 0){
        printf("Este n�mero � Par");
        par();
    }
    else {
        printf("Este n�mero � Impar");
        impar();
    }
}