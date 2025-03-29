# include <stdio.h>
# include <string.h>
# include <locale.h>

typedef struct {
    float n1,n2,n3;
} Notas;

Notas notas; // Variável Global para guardar as notas no Struct

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
    printf("Escolha o tipo de média (A para Aritmética, P para Ponderada): ");
    scanf(" %c", &opcao); // Espaço antes de %c para evitar problemas com ENTER
    linha();
    return opcao;
}

void erro(){
    printf("Opção Inválida! Tente Novamente!");
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

    char opcao = menuMedia(); // Variável para receber o retorno do menuMedia

    switch (opcao) {
        case 'A':
         resultado = mediaA(notas.n1, notas.n2, notas.n3); // 1 - Criando variável para pegar o resultado, 2 - Chamando a função e passando os valores que eu guardei no Struct
         printf("Média Aritimética: %.2f", resultado);
            break;

        case 'P':
         resultado = mediaP(notas.n1, notas.n2, notas.n3); // 1 - Criando variável para pegar o resultado, 2 - Chamando a função e passando os valores que eu guardei no Struct
         printf("Média Ponderada: %.2f", resultado);
            break;

        default:
         erro();
            break;
    }
}