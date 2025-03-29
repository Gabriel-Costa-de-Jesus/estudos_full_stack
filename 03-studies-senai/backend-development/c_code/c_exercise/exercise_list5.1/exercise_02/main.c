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

    printf("Digite um número: ");
    scanf("%d", &n1);

    if (n1 % 2 == 0){
        printf("Este número é Par");
        par();
    }
    else {
        printf("Este número é Impar");
        impar();
    }
}