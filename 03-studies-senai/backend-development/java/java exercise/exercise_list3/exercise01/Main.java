package exercise01;

import java.util.Scanner;

public class Main {
    public int menu(){
        Scanner sc = new Scanner(System.in);
        System.out.println("\nEscolha uma opção: ");
        System.out.println("1- Envelhecer");
        System.out.println("2- Engordar");
        System.out.println("3- Emagrecer");
        System.out.println("4- Altura");
        System.out.println("5- Sair");
        return sc.nextInt();

    }
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int opcao;


        do {
            opcao = menu();
            switch (opcao) {
                case 1:

                    break;
            }
        } while(opcao != 5);
    }

}
