package exercise_list3.exercise04;

import java.util.Scanner;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static Carro cc = new Carro();
    public static int menu(){
        System.out.println("\nEscolha uma oção abaixo:");
        System.out.println("1 - Andar");
        System.out.println("2 - Abastecer");
        System.out.println("3 - Desligar o carro");
        System.out.print("Digite a sua opção: ");
        int opcao = sc.nextInt();
        sc.nextLine(); // Limpando cmd caso precise
        return opcao;
    }
    public static void opAndar(){
        System.out.print("Digite a quantidade de KM do pecurso: ");
        double km = sc.nextDouble();
        cc.andar(km* cc.getConsumo());
        System.out.printf("\nVrum Vrum! Você gastou %.2f litros neste percuso! ", km*cc.getConsumo());
    }
    public static void opAbastecer(){
        System.out.print("Digite a quantidade de litros que você deseja Abastecer: ");
        double litros = sc.nextDouble();
        cc.abastecer(litros);
        System.out.printf("\nVocê absteceu %.2f litros! ", litros);
    }
    public static void erro(){
        System.out.println("Opção Inválida! Tente Novamente!");
    }
    public static void desligando(){
        System.out.print("\nDesligando o carro!");
    }
    public static void main(String[]args){
        int opcao;
        do {
            opcao = menu();
            switch (opcao){
                case 1:
                    opAndar();
                    break;
                case 2:
                    opAbastecer();
                    break;
                case 3:
                    desligando();
                    break;
                default:
                    erro();
                    break;
            }
        } while(opcao != 3);

    }
}
