package exercise01;

import java.util.Scanner;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static Pessoa ps = new Pessoa();

    public static int menu(){
        System.out.println("\nEscolha uma opção: ");
        System.out.println("1- Envelhecer");
        System.out.println("2- Engordar");
        System.out.println("3- Emagrecer");
        System.out.println("4- Altura");
        System.out.println("5- Sair");
        return sc.nextInt();

    }
    public static void cadastrar(){
        System.out.println("Digite seu nome: ");
        String nome = sc.nextLine();
        System.out.println("Digite a sua idade: ");
        int idade = sc.nextInt();
        System.out.println("Digite a seu peso:");
        double peso = sc.nextDouble();
        System.out.println("Digite a sua altura: ");
        double altura = sc.nextDouble();
        sc.nextLine();
        ps = new Pessoa(nome, idade, peso, altura);
    }
    public static void opEnvelhecer() {
        System.out.println("Digite quantos anos você deseja envelhecer: ");
        int envelhecer = sc.nextInt();

        if (ps.getIdade() < 18) {
            ps.crescer(0.5*envelhecer);
            System.out.printf("Você envelheceu %d anos e cresceu %.2f metros", envelhecer, ps.getAltura());
        }
        ps.envelhecer(envelhecer);
    }
    public static void opEngordar(){
        System.out.println("Digite quantos KG você deseja engordar");
        double kg = sc.nextDouble();
        ps.engordar(kg);
        System.out.printf("\nVocê engordou %.2f kg Totalizando %.2f Kg", kg, ps.getPeso());
    }
    public static void opEmagrecer(){
        System.out.println("Digite quantos KG você deseja emagrecer");
        double kg = sc.nextDouble();
        ps.emagrecer(kg);
        System.out.printf("\nVocê emagrecer %.2f Kg Totalizando %.2f Kg", kg, ps.getPeso());
    }
    public static void opCrescer(){
        System.out.println("Digite quantos cm ou metros que você deseja crescer");
        double kg = sc.nextDouble();
        ps.crescer(kg);
        System.out.printf("\nVocê cresceu %.2f cm Totalizando %.2f metros", kg, ps.getAltura());
    }
    public static void erro(){
        System.out.println("Opção inválida! Tente Novamente!");
    }
    public static void sair(){
        System.out.println("\nSaindo do Sistema!");
    }
    public static void main(String[]args){

        int opcao;
        cadastrar();

        do {

            opcao = menu();
            switch (opcao) {
                case 1:
                    opEnvelhecer();
                    break;
                case 2:
                    opEngordar();
                    break;
                case 3:
                    opEmagrecer();
                    break;
                case 4:
                    opCrescer();
                    break;
                case 5:
                    sair();
                    break;
                default:
                    erro();
                    break;
            }
        } while(opcao != 5);
    }

}
