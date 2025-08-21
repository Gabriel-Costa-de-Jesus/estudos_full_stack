package exercise03;

import java.util.Scanner;

public class nextLine {
    public static void main(String[]args) {

        Scanner sc = new Scanner (System.in);
        String n1,n2,n3;
        int numero;
        // Importante, se tiver por exemplo next int e dps next line, deve se usar um nextline vazio afim de evitar erros
        // Isso se chama limpar buffer de leitura
        System.out.println("Digite um número:");
        numero = sc.nextInt();
        sc.nextLine();
        System.out.println("Digite 3 coisas aleatórias:");
        n1 = sc.nextLine();
        n2 = sc.nextLine();
        n3 = sc.nextLine();
        System.out.printf("Você digitou: %d | %s | %s | %s", numero, n1, n2, n3);

    }
}
