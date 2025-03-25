# include <stdio.h>
# include <string.h>
# include <locale.h>

typedef struct {
    float n1,n2,n3;
} Notas;

Notas notas; // Vari�vel Global para guardar as notas no Struct

float mediaA(float nota1, float nota2, float nota3){ 
    return  (nota1 + nota2 + nota3) / 3;
}

float mediaP(float nota1, float nota2, float nota3) {
    return ((nota1*5) + (nota2*3) + (nota3*2)) / (5 + 3 + 2);
}

void linha() {
    for (int i = 0; i < 30; i++ ) {
        printf("--");
    } printf("\n");
}

void menuNotas() {

   linha();
   printf("Digite a primeira nota do aluno: ");
   scanf("%f", &notas.n1);

   printf("Digite a segunda nota do aluno: ");
   scanf("%f", &notas.n2);

   printf("Digite a terceira nota do aluno: ");
   scanf("%f", &notas.n3);
   linha();
    
}

int menuMedia() {
    char opcao;
    printf("Escolha o tipo de m�dia (A para Aritm�tica, P para Ponderada): ");
    scanf(" %c", &opcao); // Espa�o antes de %c para evitar problemas com ENTER
    linha();
    return opcao;
}

void erro(){
    printf("Op��o Inv�lida! Tente Novamente!");
}

// int replace(text){
//     char replaceText;
//     replaceText = (text, 'a', 'A'); IMPLEMENTAR DEPOIS QUANDO TIVER TEMPO
//     replaceText = (text, 'p', 'P');
//     return replaceText;
// }

int main() {
    setlocale(LC_ALL, "Portuguese");

    float resultado;

    menuNotas();

    char opcao = menuMedia(); // Vari�vel para receber o retorno do menuMedia

    switch (opcao) {
        case 'A':
         resultado = mediaA(notas.n1, notas.n2, notas.n3); // 1 - Criando vari�vel para pegar o resultado, 2 - Chamando a fun��o e passando os valores que eu guardei no Struct
         printf("M�dia Aritim�tica: %.2f", resultado);
            break;

        case 'P':
         resultado = mediaP(notas.n1, notas.n2, notas.n3); // 1 - Criando vari�vel para pegar o resultado, 2 - Chamando a fun��o e passando os valores que eu guardei no Struct
         printf("M�dia Ponderada: %.2f", resultado);
            break;

        default:
         erro();
            break;
    }
}