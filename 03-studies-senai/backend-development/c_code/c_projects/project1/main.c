// Bibliotecas Necessárias
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <locale.h>
#include <ctype.h>
#include <time.h>

// Definindo o Struct
struct SupermercadoSystem {
   char nomeProduto[50];
   float precoProduto;
   int codigoProduto;
}; struct SupermercadoSystem sistema[5];

// Declarando Variáveis Globais
int contador = 0; //Core

// Chamando Protótipos de Funções
void replace_and_convert(char * txt);
void pressAnyKey();

// Funções principais do meu sistema
int menu(){
    int opcao;
    printf("\nEscolha uma opção abaixo");
    printf("\n1 - Cadastrar Produto");
    printf("\n2 - Listar Produtos Cadastrados");
    printf("\n3 - Buscar Produtos");
    printf("\n4 - Apagar Produtos");
    printf("\n5 - Alterar Produtos");
    printf("\n6 - Cadastrar Cliente");
    printf("\n7 - Listar Clientes Cadastrados");
    printf("\n8 - Buscar Clientes");
    printf("\n9 - Apagar Cliente");
    printf("\n10 - Alterar Cliente");  
    printf("\n11 - Registar compra");
    printf("\n12 - Limpar Tela");
    printf("\n13 - Sair do Sistema");
    printf("\nEscolha sua opção: ");
    scanf("%d", &opcao);

    return opcao;
}

void cadastrarProduto(){
    fflush(stdin); 

    char inputDate[50];
    printf("\nDigite o nome do Produto para ser cadastrado: ");
    fgets(sistema[contador].nomeProduto, 50, stdin);
    sistema[contador].nomeProduto[strcspn(sistema[contador].nomeProduto, "\n")] = '\0'; // Remove o '\n'


    printf("\nDigite o preço do Produto para ser cadastrado: ");
    scanf("%s", inputDate);
    replace_and_convert(inputDate); // Troca . por , para não causar erro
    sistema[contador].precoProduto = strtof(inputDate, NULL); // Converte char para float
    sistema[contador].codigoProduto = ((int)time(NULL) % 100000) + contador; // A biblioteca Time retorna o número de segundos desde 1º de janeiro de 1970, o Objetivo de sua implementação era apenas pra ficar gerando números únicos para servir de código, o + contador no final é para garantir que nunca iria se repetir, pois essa função se baseia no tempo de agora
    
    printf("\nProduto Cadastrado Com Sucesso!");
    contador++;
    
}

void listarProdutos(){
    if (contador == 0){
        printf("\nCadastre algum Produto Primeiro!");
        return;
    }

    printf("\nProdutos Cadastrados no Sistema!");
    for (int i = 0; i < contador; i++) {
        printf("\n\nProduto: %s",sistema[i].nomeProduto);
        printf("\nPreço: %.2f",sistema[i].precoProduto);
        printf("\nCódigo de Produto: %d",sistema[i].codigoProduto);
    }
    pressAnyKey();
}

void buscarProdutos() {
    if (contador == 0){
        printf("\nCadastre algum Produto Primeiro!");
        return;
    }
    fflush(stdin);
    char produtoNome[50];

    printf("Digite o nome do produto ou código do sistema: ");
    fgets(produtoNome, 50, stdin);
    produtoNome[strcspn(produtoNome, "\n")] = '\0'; // O fgets adiciona uma linha no final, isso remove
// O strcspn procura um caractere com base no indice, nesse caso ele procura a linha e remove

    int codigoBuscado = atoi(produtoNome); // atoi serve para converter um char em int, da mesma forma que faço com strtof onde converto char para float 

    replace_and_convert(produtoNome);
  
    for (int i = 0; i < contador; i++) {
        char produto[50];
        strcpy(produto, sistema[i].nomeProduto);
        replace_and_convert(produto);
        
        if (strcmp(produtoNome, produto) == 0 || codigoBuscado == sistema[i].codigoProduto) {
            printf("\nProduto Encontrado!");
            printf("\nNome: %s", sistema[i].nomeProduto);
            printf("\nPreço: %.2f", sistema[i].precoProduto);
            printf("\nCódigo: %d\n", sistema[i].codigoProduto);
            pressAnyKey();
            return; 
        }
    }

    printf("\nProduto Não encontrado no Sistema");
}

void apagarProduto() {
    if (contador == 0) {
        printf("\nNenhum produto cadastrado!\n");
        return;
    }

    fflush(stdin);

    char produtoNome[50];
    printf("\nDigite o nome do produto que deseja apagar ou o código: ");
    fgets(produtoNome, 50, stdin);
    produtoNome[strcspn(produtoNome, "\n")] = '\0';  // Remove o '\n'

    int codigoBuscar = atoi(produtoNome);

    replace_and_convert(produtoNome);

    for (int i = 0; i < contador; i++) {
        char produto[50]; 
        strcpy(produto, sistema[i].nomeProduto);
        replace_and_convert(produto);
        
        if (strcmp(produtoNome, produto) == 0 || codigoBuscar == sistema[i].codigoProduto) {
            printf("Produto %s Removido com sucesso!", produto);
            sistema[i] = sistema[contador -1]; // Troca o que está nessa posição pelo último item adicionado
            contador--; // Atualiza o contador
            pressAnyKey();
            return;
        }
    }
    printf("Produto não encontrado no sistema!");
}

void alterarProdutos(){
    if (contador == 0) {
        printf("\nNenhum produto cadastrado!\n");
        return;
    }

    listarProdutos();

    fflush(stdin);

    char produtoNome[50];
    printf("\n\nDigite o nome do Produto que você deseja alterar: ");
    fgets(produtoNome, 50, stdin);
    produtoNome[strcspn(produtoNome, "\n")] = '\0';

    int codigoBuscar = atoi(produtoNome);
    
    replace_and_convert(produtoNome);

    for (int i = 0; i < contador ; i++) {
        char produto[50];
        strcpy(produto, sistema[i].nomeProduto);
        replace_and_convert(produto);

        if (strcmp(produtoNome, produto) == 0 || codigoBuscar == sistema[i].codigoProduto) {
            fflush(stdin); 

            char inputDate[50];
            printf("\nDigite o nome do novo Produto: ");
            fgets(sistema[i].nomeProduto, 50, stdin);
            sistema[i].nomeProduto[strcspn(sistema[i].nomeProduto, "\n")] = '\0'; // Remove o '\n'
        
        
            printf("\nDigite o preço do novo Produto: ");
            scanf("%s", inputDate);
            replace_and_convert(inputDate);
            sistema[i].precoProduto = strtof(inputDate, NULL);
            sistema[i].codigoProduto = ((int)time(NULL) % 100000) + contador; 
            
            printf("\nProduto Alterado Com Sucesso!");
            return;
        }
    }
    printf("\nProduto Não encontrado no Sistema");
}
// Funções Auxiliares
void replace_and_convert(char * txt) { //Minha função para formatação de dados
    for (int i = 0; txt[i] != '\0'; i++) {
        if (txt[i] == '.'){ // Função para troca de caractere
            txt[i] = ',';
        }
        txt[i] = toupper(txt[i]); // Função para converter para Maiúsculo
    }
}
void sair() {
    printf("Saindo do Sistema");
    for (int i = 0; i < 5; i++) {
        printf(".");
        sleep(1);
    }
    printf("\nAgradecemos por utilizar nosso Sistema!");
    sleep(3);
    system("cls");
}

void erro() {
    printf("Opção Inválida! Tente Novamente! \n");
}
void clearDelay(){
    printf("Limpando a Tela");
    for (int i = 0; i < 5; i++) {
        printf(".");
        sleep(1);
    }
    printf("\nSistema Limpo! Agradecemos pela a sua Paciência...");
    sleep(3);
    system("cls");
}
void pressAnyKey(){
    printf("\nPressione qualquer tecla e em seguida Enter para continuar. . .");
    getchar(); // Captura a tecla pressionada
    getchar(); // Para evitar problemas com o buffer
}
// Função Principal Main
int main() {

    setlocale(LC_ALL, "Portuguese");
    
    printf("Seja bem vindo ao sistema de cadastramento de Produtos!\n");

    int opcao;
    do{
        
        opcao = menu();

        switch (opcao) {
        case 1:
            cadastrarProduto();
            break;
        case 2:
            listarProdutos();
            break;
        case 3:
            buscarProdutos();
            break;
        case 4:
            apagarProduto();
            break;
        case 5:
            alterarProdutos();
            break;
        case 12:
            clearDelay();
            break;
        case 13:
            sair();
            break;
        default:
            erro();
            break;
        }

        sleep(3);
        system("cls");
    } while (opcao != 13);
}