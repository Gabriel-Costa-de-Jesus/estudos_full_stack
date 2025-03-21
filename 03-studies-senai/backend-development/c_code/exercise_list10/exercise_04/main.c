# include <stdio.h>
# include <locale.h>

int main(){

    setlocale(LC_ALL, "Portuguese");

    int value[5];

    printf("Digite 5 números Inteiros\n");
    for(int count = 0; count < 5; count++) {
        printf("Número[%d]: ", count + 1);
        scanf("%d", &value[count]);

        if (count == 4){
            printf("Valores Invertidos:\n");
            for(int count = 5; count > -1; count--) {
               printf("%d", value[count]);
               printf("\n");
             }
         }
    }
}