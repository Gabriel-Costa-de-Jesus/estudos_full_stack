package exercise06;

import java.util.Scanner;

public class switchcase {
    public static void main(String[]args){

        Scanner sc = new Scanner(System.in);
        System.out.println("Qual sabor você prefere?");
        System.out.println("1 - Morango");
        System.out.println("2 - Chocolate");
        int opcao = sc.nextInt();

        switch(opcao) {
            case 1:
                System.out.print("Você escolheu Morango");
                break;
            case 2:
                System.out.print("Você escolheu Chocolate");
                break;
            default:
                System.out.print("Opção Inválida");
                break;
        }
        sc.close();


    }
}
