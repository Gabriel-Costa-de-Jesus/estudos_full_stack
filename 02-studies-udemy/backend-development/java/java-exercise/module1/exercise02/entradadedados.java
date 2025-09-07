package exercise02;

import java.util.Scanner;

public class entradadedados {
    public static void main(String[]args) {
        Scanner sc = new Scanner(System.in);

        String nome;
        int idade;
        double altura;
        // Sc;next funciona apenas para nomes simples, nomes com sobrenomes por exemplo não funciona
        System.out.print("Digite seu nome: ");
        nome = sc.next();
        System.out.print("Digite a sua idade: ");
        idade = sc.nextInt();
        System.out.print("Digite a sua altura: ");
        altura = sc.nextDouble();
        System.out.printf("Seu nome é: %s você tem %d anos e tem %.2f%n Metros de altura", nome, idade, altura);

        sc.close();
    }
}