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
   char nomeProduto[50], nomeCliente[50], cpfCliente[15];
   float precoProduto, compraCliente;
   int codigoProduto, estoqueProduto;
}; struct SupermercadoSystem sistema[5];

// Declarando Variáveis Globais
int contadorProduto = 0, contadorCliente =0, contadorCompra = 0; //Core

// Chamando Protótipos de Funções
void replace_and_convert(char * txt);
void pressAnyKey();
void erro();

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
    fgets(sistema[contadorProduto].nomeProduto, 50, stdin);
    sistema[contadorProduto].nomeProduto[strcspn(sistema[contadorProduto].nomeProduto, "\n")] = '\0'; // Remove o '\n'
    

    printf("\nDigite o preço do Produto para ser cadastrado: ");
    scanf("%s", inputDate);
    replace_and_convert(inputDate); // Troca . por , para não causar erro
    sistema[contadorProduto].precoProduto = strtof(inputDate, NULL); // Converte char para float 
    sistema[contadorProduto].codigoProduto = ((int)time(NULL) % 100000) + contadorProduto; // A biblioteca Time retorna o número de segundos desde 1º de janeiro de 1970, o Objetivo de sua implementação era apenas pra ficar gerando números únicos para servir de código, o + contadorProduto no final é para garantir que nunca iria se repetir, pois essa função se baseia no tempo de agora
    
    printf("\nDigite a Quantidade de produto no estoque: ");
    scanf("%d", &sistema[contadorProduto].estoqueProduto);

    printf("\nProduto Cadastrado Com Sucesso!");
    contadorProduto++;
    
}

void listarProdutos(){
    if (contadorProduto == 0){
        printf("\nCadastre algum Produto Primeiro!");
        return;
    }

    printf("\nProdutos Cadastrados no Sistema!");
    for (int i = 0; i < contadorProduto; i++) {
        printf("\n\nProduto: %s",sistema[i].nomeProduto);
        printf("\nPreço: %.2f",sistema[i].precoProduto);
        printf("\nCódigo de Produto: %d",sistema[i].codigoProduto);
        printf("\nQuantidade no estoque: %d",sistema[i].estoqueProduto);
    }
    pressAnyKey();
}

void buscarProdutos() {
    if (contadorProduto == 0){
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
  
    for (int i = 0; i < contadorProduto; i++) {
        char produto[50];
        strcpy(produto, sistema[i].nomeProduto);
        replace_and_convert(produto);
        
        if (strcmp(produtoNome, produto) == 0 || codigoBuscado == sistema[i].codigoProduto) {
            printf("\nProduto Encontrado!");
            printf("\nNome: %s", sistema[i].nomeProduto);
            printf("\nPreço: %.2f", sistema[i].precoProduto);
            printf("\nCódigo: %d\n", sistema[i].codigoProduto);
            printf("\nQuantidade no estoque: %d",sistema[i].estoqueProduto);
            pressAnyKey();
            return; 
        }
    }

    printf("\nProduto Não encontrado no Sistema");
}

void apagarProduto() {
    if (contadorProduto == 0) {
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

    for (int i = 0; i < contadorProduto; i++) {
        char produto[50]; 
        strcpy(produto, sistema[i].nomeProduto);
        replace_and_convert(produto);
        
        if (strcmp(produtoNome, produto) == 0 || codigoBuscar == sistema[i].codigoProduto) {
            printf("Produto %s Removido com sucesso!", produto);
            sistema[i] = sistema[contadorProduto -1]; // Troca o que está nessa posição pelo último item adicionado
            contadorProduto--; // Atualiza o contadorProduto
            pressAnyKey();
            return;
        }
    }
    printf("Produto não encontrado no sistema!");
}

void alterarProdutos(){
    if (contadorProduto == 0) {
        printf("\nNenhum Produto Cadastrado!");
        return;
    }

    fflush(stdin);
    char produtoNome[50];

    printf("Digite o nome do produto ou código do sistema: ");
    fgets(produtoNome, 50, stdin);
    produtoNome[strcspn(produtoNome, "\n")] = '\0'; 

    int codigoBuscado = atoi(produtoNome);

    replace_and_convert(produtoNome);
  
    for (int i = 0; i < contadorProduto; i++) {
        char produto[50];
        strcpy(produto, sistema[i].nomeProduto);
        replace_and_convert(produto);
        
        if (strcmp(produtoNome, produto) == 0 || codigoBuscado == sistema[i].codigoProduto) {
            int opcaoProduto;
            printf("\nO que você deseja alterar?");
            printf("\n1 - Nome do Produto: ");
            printf("\n2 - Preço do Produto: ");
            printf("\n3- Estoque do Produto");
            printf("\nEscolha uma opção: ");
            scanf("%d", &opcaoProduto);

            fflush(stdin);

            switch (opcaoProduto) {
            case 1:
                printf("\nDigite o novo nome do Produto: ");
                fgets(sistema[i].nomeProduto, 50, stdin);
                sistema[i].nomeProduto[strcspn(sistema[i].nomeProduto, "\n")] = '\0';
                break;
            case 2:
                 printf("\nDigite o novo preço do Produto: ");
                 scanf("%f", &sistema[i].precoProduto);
                 break;
            case 3:
                printf("\nDigite a nova quantidade do estoque do Produto: ");
                scanf("%d", &sistema[i].estoqueProduto);
                break;
            default:
                printf("\nOpção Inválida: ");
                break;
            }

            printf("\nProduto %s Alterado com Sucesso!", sistema[i].nomeProduto);     
            return;
        }
    }
      printf("Cliente não encontrado! ");
}

void cadastrarCliente(){

    fflush(stdin);
    printf("\nDigite o nome do cliente para ser cadastrado: ");
    fgets(sistema[contadorCliente].nomeCliente, 50, stdin);
    sistema[contadorCliente].nomeCliente[strcspn(sistema[contadorCliente].nomeCliente, "\n")] = '\0';

    printf("\nDigite o CPF do cliente para ser cadastrado: ");
    scanf("%s", sistema[contadorCliente].cpfCliente);

    printf("\nCliente Cadastrado com Sucesso!");
    contadorCliente++;
}

void listarClientes() {
    if (contadorCliente == 0) {
        printf("\nNenhum Cliente Cadastrado!");
        return;
    }

    printf("\nClientes Cadastrados no Sistema: \n");
    for (int i = 0; i < contadorCliente; i++) {
        printf("\nCliente: %s", sistema[i].nomeCliente);
        printf("\nCPF: %s", sistema[i].cpfCliente);
    }

    pressAnyKey();
}

void buscarCliente() {
    if (contadorCliente == 0) {
        printf("\nNenhum Cliente Cadastrado!");
        return;
    }

    fflush(stdin);

    char clienteBuscar[50], cpfBuscar[15];
    printf("\nDigite o nome do cliente ou CPF: ");
    fgets(clienteBuscar, 50, stdin);
    clienteBuscar[strcspn(clienteBuscar, "\n")] = '\0';
    //char cpfBuscar[15] = clienteBuscar[50]; Em C não pode se comparar dessa forma pois são vetores
    strcpy(cpfBuscar, clienteBuscar);
    

    replace_and_convert(clienteBuscar);

    for (int i = 0; i < contadorCliente; i++){

        char clienteBuscado[50];
        strcpy(clienteBuscado, sistema[i].nomeCliente);
        replace_and_convert(clienteBuscado);
        
        if (strcmp(clienteBuscado, clienteBuscar) == 0 || strcmp(cpfBuscar, sistema[i].cpfCliente) == 0) {
            printf("\nCliente %s Encontrado!", sistema[i].nomeCliente);
            printf("\n Histórico de Compras, Dados do cliente, endereço de entrega, contato"); // Talvez faça furutamente

            pressAnyKey();
            return;
        }
    }
      printf("Cliente não encontrado! ");
}

void apagarCliente() {
    if (contadorCliente == 0) {
        printf("\nNenhum Cliente Cadastrado!");
        return;
    }

    fflush(stdin);

    char clienteBuscar[50], cpfBuscar[15];
    printf("\nDigite o nome do cliente ou CPF: ");
    fgets(clienteBuscar, 50, stdin);
    clienteBuscar[strcspn(clienteBuscar, "\n")] = '\0';
    //char cpfBuscar[15] = clienteBuscar[50];
    strcpy(cpfBuscar, clienteBuscar);
    

    replace_and_convert(clienteBuscar);

    for (int i = 0; i < contadorCliente; i++){

        char clienteBuscado[50];
        strcpy(clienteBuscado, sistema[i].nomeCliente);
        replace_and_convert(clienteBuscado);
        
        if (strcmp(clienteBuscado, clienteBuscar) == 0 || strcmp(cpfBuscar, sistema[i].cpfCliente) == 0) {
            printf("Cliente %s Apagado com Sucesso!", sistema[i].nomeCliente);
            sistema[i] = sistema[contadorCliente -1]; // Copia o item da última posição
            contadorCliente--;  
            return;
        }
    }
      printf("Cliente não encontrado! ");
}

void alterarCliente() {
    if (contadorCliente == 0) {
        printf("\nNenhum Cliente Cadastrado!");
        return;
    }

    fflush(stdin);

    char clienteBuscar[50], cpfBuscar[15];
    printf("\nDigite o nome do cliente ou CPF: ");
    fgets(clienteBuscar, 50, stdin);
    clienteBuscar[strcspn(clienteBuscar, "\n")] = '\0';
    //char cpfBuscar[15] = clienteBuscar[50];
    strcpy(cpfBuscar, clienteBuscar);
    

    replace_and_convert(clienteBuscar);

    for (int i = 0; i < contadorCliente; i++){

        char clienteBuscado[50];
        strcpy(clienteBuscado, sistema[i].nomeCliente);
        replace_and_convert(clienteBuscado);
        
        if (strcmp(clienteBuscado, clienteBuscar) == 0 || strcmp(cpfBuscar, sistema[i].cpfCliente) == 0) {
            int opcaoCliente;
            printf("\nO que você deseja alterar?");
            printf("\n1 - Nome do Cliente:");
            printf("\n2 - CPF do cliente:");
            printf("\nEm breve novas opções...");
            printf("\nEscolha uma opção: ");
            scanf("%d", &opcaoCliente);

            fflush(stdin);

            switch (opcaoCliente) {
            case 1:
                printf("\nDigite o novo nome do Cliente: ");
                fgets(sistema[i].nomeCliente, 50, stdin);
                sistema[i].nomeCliente[strcspn(sistema[i].nomeCliente, "\n")] = '\0';
                break;
            case 2:
                 printf("\nDigite o CPF do cliente para ser cadastrado: ");
                 scanf("%s", sistema[i].cpfCliente);
                 break;
            default:
                printf("\nOpção Inválida: ");
                break;
            }

            printf("\nCliente %s Alterado com Sucesso!", sistema[i].nomeCliente);     
            return;
        }
    }
      printf("Cliente não encontrado! ");
}

void registrarCompra() {
    if (contadorCliente == 0) {
        printf("\nNenhum Cliente Cadastrado!");
        return;
    }
    else if (contadorProduto == 0) {
        printf("\nNenhum Produto Cadastrado!");
        return;
    }

    fflush(stdin);
    
    printf("\nClientes Cadastrados no Sistema: \n");
    for (int i = 0; i < contadorCliente; i++) {
        printf("\nCliente: %s", sistema[i].nomeCliente);
        printf("\nCPF: %s", sistema[i].cpfCliente);
    }

        
            char clienteComprar[50], clienteComprarCPF[15];
            printf("\nDigite o nome do Cliente ou CPF que irá efetuar a compra: ");
            fgets(clienteComprar, 50, stdin);
            clienteComprar[strcspn(clienteComprar, "\n")] = '\0';

            strcpy(clienteComprarCPF, clienteComprar);

            replace_and_convert(clienteComprar);
            for (int i = 0; i < contadorCliente; i++) {
                replace_and_convert(sistema[i].nomeCliente);
                

                if (strcmp(clienteComprar, sistema[i].nomeCliente) == 0 || strcmp(clienteComprarCPF, sistema[i].cpfCliente) == 0) {

                    contadorCompra = i; // Apenas para saber a posição do cliente no vetor
                    printf("\nCliente %s Selecionado", sistema[i].nomeCliente);

                    printf("\n\nProdutos Cadastrados no Sistema!");
                    for (int i = 0; i < contadorProduto; i++) {
                        printf("\n\nProduto: %s",sistema[i].nomeProduto);
                        printf("\nPreço: %.2f",sistema[i].precoProduto);
                        printf("\nCódigo de Produto: %d",sistema[i].codigoProduto);
                        printf("\nQuantidade no estoque: %d",sistema[i].estoqueProduto);
                    }
                
                    int produtoOpcao;
                    float soma = 0;

                    do {
                        printf("\n\nO que você deseja fazer?");
                        printf("\n1 - Lançar Produto");
                        printf("\n2 - Fechar Comprar");
                        printf("\nEscolha sua opção: ");
                        scanf("%d", &produtoOpcao);

                        int produtocodigo; // Não pode declarar dentro do Switch
                     

                        switch (produtoOpcao) {
                        case 1:
                            printf("\nDigite o código do produto: ");
                            scanf("%d", &produtocodigo);
                            
        
                            for (int i = 0; i < contadorProduto; i++) {
                                if (produtocodigo == sistema[i].codigoProduto) {
                                    printf("\n\nProduto: %s Preço R$ %.2f", sistema[i].nomeProduto, sistema[i].precoProduto);
                                    soma += sistema[i].precoProduto;
                                    printf("\nTotal da Compra: R$ %.2f", soma);
                                    sistema[contadorCompra].compraCliente = soma; 
                                    sistema[i].estoqueProduto--;
                                }
                            }
                            break;
                        case 2:
                            printf("\n\nCompra Finalizada! Total: %.2f", sistema[contadorCompra].compraCliente);
                            break;
                        
                        default:
                            erro();
                            break;
                        }
                        
                    } while (produtoOpcao != 2);           
                }

           }  
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
    printf("\n\nPressione qualquer tecla e em seguida Enter para continuar. . .");
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
        case 6:
            cadastrarCliente();
            break;
        case 7:
            listarClientes();
            break;
        case 8:
            buscarCliente();
            break;
         case 9:
            apagarCliente();
            break;    
        case 10:
            alterarCliente();
            break;
        case 11:
            registrarCompra();
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

        sleep(2);
        system("cls");
    } while (opcao != 13);
}