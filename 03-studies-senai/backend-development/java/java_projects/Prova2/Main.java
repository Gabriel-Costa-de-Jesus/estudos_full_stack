package Prova2;

import java.util.Scanner;

public class Main {
    static Tamagushi tm = new Tamagushi();
    static Scanner sc = new Scanner(System.in);
    public static int menu(){
        System.out.println("\nEscolha uma opção abaixo:");
        System.out.println("1 - Brincar");
        System.out.println("2 - Alimentar");
        System.out.println("3 - Verificar Humor");
        System.out.println("4 - Sair");
        System.out.print("Escolha uma opção: ");
        int opcao = sc.nextInt();
        sc.nextLine();
        return opcao;
    }
    public static void cadastrar(){
        System.out.println("\nSeja bem vindo (a) ao nosso programa!");
        System.out.println("Para começar cadastre as informações do seu bichinho\n");

        System.out.print("Digite o nome do seu bichinho: ");
        String nome = sc.nextLine();
        System.out.print("Digite a idade do seu bichinho: ");
        int idade = sc.nextInt();
        Tamagushi tm = new Tamagushi(nome, idade);
        System.out.println("\nBichinho cadastrado com sucesso!");
    }
    public static void opBrincar(){
        System.out.println("Por quanto tempo você deseja brincar? ");
        double minutos = sc.nextDouble();
        tm.brincar(minutos);
    }
    public static void opAlimentar(){
        System.out.println("Quanto de comida você deseja Alimentar?");
        double quantidade = sc.nextDouble();
        tm.alimentar(quantidade);
    }
    public static void opHumor(){
        System.out.println("Vamos verificar o humor do seu bichinho\n");
        System.out.printf("%nNível de Fome: %.2f", tm.getFome());
        System.out.printf("%nNível de Tédio: %.2f", tm.getTedio());
        System.out.printf("%nNível de Humor: %.2f%n", tm.getHumor());

        if (tm.getHumor() >= 50 && tm.getHumor() < 100){
            System.out.println("\nStatus do bichinho: Feliz :0");
        }
        else if (tm.getHumor() >= 100 && tm.getHumor() < 150){
            System.out.println("\nStatus do bichinho: Triste :(");
        }
        else if (tm.getHumor() >= 150){
            System.out.println("\nStatus do bichinho: Irritado");
        }

    }
    public static void sair(){
        System.out.print("\nSaindo do Sistema...");
    }
    public static void erro(){
        System.out.print("Opção inválida! Tente Novamente");
    }
    public static void main(String[]args){
        int opcao;
        cadastrar();
        do {
            opcao = menu();
            switch (opcao){
                case 1:
                    opBrincar();
                    break;
                case 2:
                    opAlimentar();
                    break;
                case 3:
                    opHumor();
                    break;
                case 4:
                    sair();
                    break;
                default:
                    erro();
                    break;
            }
        } while(opcao != 4);
    }
}
