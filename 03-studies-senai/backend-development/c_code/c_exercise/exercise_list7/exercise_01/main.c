#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <locale.h>

#define MAX_SYSTEM 500
#define MIN_PASSWORD 8

struct Registration {
	   char name[50], tel[15], email[50], user[25], passWord[25];
       int age;
}; struct Registration userSystem[MAX_SYSTEM];

// Vari�veis globais
int countUser = 0;
// Prot�tipo de Sistema
void pressAnyKey();
// Fun��es principais
int menu(){
	int option;
	printf("\nEscolha uma op��o abaixo: ");
	printf("\n1 - Cadastrar usu�rio");
	printf("\n2 - Listar usu�rios cadastrados");
	printf("\n3 - Sair do Sistema");
	printf("\nEscolha uma op��o: ");
	scanf("%d", &option);
	while (getchar() != '\n');
	return option;
}

void registerr() {
	if (countUser >= MAX_SYSTEM){
		printf("\nLimite Atinjido");
	    return;
	}
	
	char checkUser[50], checkPassWord[50];
	int userNumber =0, passWordNumber =0;
	
	printf("\nDigite o seu nome: ");
	fgets(userSystem[countUser].name, 50, stdin);
	userSystem[countUser].name[strcspn(userSystem[countUser].name, "\n")] = '\0';
	
	printf("\nDigite a sua idade: ");
	scanf("%d", &userSystem[countUser].age);
	while(getchar() != '\n');
	
	if(userSystem[countUser].age < 18){
		printf("\nAcesso Negado! Idade menor que 18!");
        return;
	}
	 
	printf("\nDigite a seu n�mero de celular: "); 		
	fgets(userSystem[countUser].tel, 15, stdin);
	userSystem[countUser].tel[strcspn(userSystem[countUser].tel, "\n")] = '\0';
	
	printf("\nDigite o seu E-mail: ");
	fgets(userSystem[countUser].email, 15, stdin);
	userSystem[countUser].email[strcspn(userSystem[countUser].email, "\n")] = '\0';
	
	while(userNumber < MIN_PASSWORD) {
		printf("\nDigite um nome de Usu�rio: ");
		fgets(checkUser, 50, stdin);
		checkUser[strcspn(checkUser, "\n")] = '\0';
		
		for(int i =0; i < 50; i++){
			if(checkUser[i] == '\0') {
		    	userNumber= i;		
			}     
		}
		 if(userNumber >= MIN_PASSWORD) {
                strcpy(userSystem[countUser].user, checkUser);
                break;
			}
	     else{
  	            printf("\nDigite um usu�rio com 8 caracteres no m�nimo! Tente Novamente! \n");
			  }								 
	}
	
	while(passWordNumber < MIN_PASSWORD){
		 printf("\nDigite uma senha: ");
		 fgets(checkPassWord, 15, stdin);
		 checkPassWord[strcspn(checkPassWord, "\n")] = '\0';
		 								    
	 	  for(int i =0; i < 15; i++){
				if(checkPassWord[i] == '\0') {
			    	passWordNumber= i;	
				
				}									   
			}
	 	  if(userNumber >= MIN_PASSWORD) {
	               strcpy(userSystem[countUser].passWord, checkPassWord);  
	               break;   
		    }
			else {
					printf("\nDigite uma senha com 8 caracteres no m�nimo! Tente Novamente! ");  									  	
				}  				 	 		 
	}
	
	printf("\nCadastrado Realizado com Sucesso!");
	countUser++;
	
}

void userList(){
	if (countUser == 0){
		printf("\nCadastre algu�m primeiro! ");
	    return;
	}
	printf("\nUsu�rios Cadastrados!\n");
	for (int i =0; i < countUser; i++) {
		printf("\nNome: %s", userSystem[i].name);
		printf("\nIdade: %d anos", userSystem[i].age);
		printf("\nCelular: %s", userSystem[i].tel);
		printf("\nE-mail: %s", userSystem[i].email);
		printf("\nUsu�rio(a): %s", userSystem[i].user);
		printf("\nSenha: %s", userSystem[i].passWord);
		printf("\n");
	}
	pressAnyKey();
}

void exitt() {
	printf("\nSaindo do Sistema");
	for (int i =0; i < 5; i++) {
		printf(".");
		sleep(1);
	} printf("\nAgradecemos por utilizar nosso Sistema!");
      sleep(2);
	
}
// Fun��es auxli�res
void clearDelay() {
	sleep(2);
	system("cls");
}

void pressAnyKey() {
	printf("\n\n");
	system("pause");
}

void error(){
	printf("\nOp��o inv�lida! Tente novamente!");
}
// Fun��o Principal
int main() {
	setlocale(LC_ALL, "Portuguese");
	
	int option;
	do{
		option = menu();
		switch (option) {
			   	case 1:
				   registerr();
				   break;
				case 2:
					 userList();
					 break;
				case 3:
					 exitt();
					 break;
				default:
					  error();
					  break;  
	    }
    	clearDelay();
	} while(option != 3);

	return 0;
}