package exercise_list3.exercise02;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static List<ContaCorrente> contas = new ArrayList<>();
    static Scanner sc = new Scanner(System.in);
    static ContaCorrente cc = new ContaCorrente();

    public static int menu(){
        System.out.println("Escolha uma opção abaixo: ");
        System.out.println("1 - Depositar: ");
        System.out.println("2 - Sacar: ");
        System.out.println("3 - Vizualizar todas as pessoas cadastradas: ");
        System.out.println("4 - Cadastrar outra pessoa: ");
        System.out.println("5 - Sair");
        System.out.print("Digite a sua opção: ");
        int opcao = sc.nextInt();
        sc.nextLine();
        return opcao;

    }
    public static void cadastro(){
        System.out.println("Digite seu nome: ");
        String nome = sc.nextLine();
        System.out.println("Digite o número da conta: ");
        int numeroDaConta = sc.nextInt();
        System.out.println("Digite o seu saldo: ");
        double saldo = sc.nextDouble();
        cc = new ContaCorrente(numeroDaConta, nome, saldo);
        contas.add(cc);
    }

    public static void opDepositar(){
        System.out.println("Digite o valor que deseja depositar: ");
        cc.depositar(sc.nextDouble());
    }
    public static void opSacar(){
        System.out.println("Digite o valor que deseja sacar: ");
        cc.sacar(sc.nextDouble());
    }
    public static void opVizualizar(){
        for (ContaCorrente c : contas) {
            System.out.println(c.toString()); // obs:mas precisa de toString() na classe ContaCorrente
        }
    }
    public static void erro(){
        System.out.println("Opção inválida! Tente Novamente!");
    }
    public static void sair(){
        System.out.println("\nSaindo do Sistema!");
    }
    public static void main(String[]args) {
        cadastro();
        int opcao;
        do {
            opcao = menu();
            switch (opcao){
                case 1:
                    opDepositar();
                    break;
                case 2:
                    opSacar();
                    break;
                case 3:
                    opVizualizar();
                    break;
                case 4:
                    cadastro();
                    break;
                case 5:
                    sair();
                    break;
                default:
                    erro();
                    break;
            }
        } while (opcao != 5);
        sc.close();
    }
}
