package exercise08;

import java.util.Scanner;

public class estruturasderepeticao {

    public static void main(String[]args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite um número para encerrar digite 0");
        int n1 = sc.nextInt();
        int soma =0;
        while(n1 != 0) {
            soma += n1;
            n1 = sc.nextInt();
        }
        System.out.printf("A soma de todos os números digitados foi: %d", soma);
        faca();
        facaenquanto();
        sc.close();
    }

    public static void faca() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite um outro número, para encerrar digite 0");
        int n1 = sc.nextInt();
        int soma =0;
        for (int i = 0; i < 5; i++) {
            soma += n1;
            n1 = sc.nextInt();
        }
        System.out.printf("A soma de todos os números digitados foi: %d", soma);
        sc.close();
    }
    
    public static void facaenquanto() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite mais um número, para encerrar digite 0");
        int n1 = sc.nextInt();
        int soma =0;
        do{
            soma += n1;
            n1 = sc.nextInt();
        } while(n1 != 0);
        System.out.printf("A soma de todos os números digitados foi: %d", soma);
        sc.close();
    }
}
