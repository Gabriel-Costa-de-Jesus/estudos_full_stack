package exercise02.Master;

import java.util.Scanner;
import java.util.Random;
import exercise02.Classes.*;

public class Main {
    public static int menuJ1() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Turno do Macaco 1 \n");
        System.out.println("Escolha uma opção Abaixo:");
        System.out.println("1 - Alimemtar macaco");
        System.out.println("2 - Ver Estômago");
        System.out.println("3- Digerir Alimento");
        System.out.println("4 - Passar Turno(Sair)");
        System.out.print("Digite uma opção: ");
        return sc.nextInt();
    }
    public static int menuJ2() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Turno do Macaco 2 \n");
        System.out.println("Escolha uma opção para Continuar");
        System.out.println("1 - Alimemtar macaco");
        System.out.println("2 - Ver Estômago");
        System.out.println("3- Digerir Alimento");
        System.out.println("4 - Passar Turno(Sair)");
        System.out.print("Digite uma opção: ");
        return sc.nextInt();
    }


    public static void main(String[]args) {
        Monkey M1 = new Monkey();
        Monkey M2 = new Monkey();
        Scanner sc = new Scanner(System.in);
        Random random = new Random();


        String nomeDoMacaco1, nomeDoMacaco2;
        int opcao, contador1 = 0, contador2 = 0;

        System.out.println("\nSeja bem vindo ao Boss Fighter!");
        System.out.println("\nCadastre um Macaco Primeiro para lutar:");
        nomeDoMacaco1 = sc.nextLine();

        M1.setCadastrarMonkey(nomeDoMacaco1);

        System.out.printf("Macaco 1 %s Cadastrado! \n", nomeDoMacaco1);

        System.out.println("\nCadastre um Segundo Macaco para lutar");
        nomeDoMacaco2 = sc.nextLine();

        M2.setCadastrarMonkey(nomeDoMacaco2);

        System.out.printf("Macaco 2 %s Cadastrado! \n", nomeDoMacaco2);

        do {
            opcao = menuJ1();
            switch (opcao) {
                case 1:
                    int numero = random.nextInt(6) + 1;
                    System.out.printf("Nesta rodada você pode alimentar %d vez(es)\n", numero);
                    for (int i = 0; i < numero; i++) {
                        System.out.print("Digite um alimento: ");
                        String alimento = sc.nextLine();
                        M1.adicionarComida(alimento);
                        contador1++;
                    }
                    break;

                case 2:
                    String[] estomagoDoMacaco = M1.getEstomago();
                    for (int i = 0; i < contador1; i++) {
                        System.out.println("Posição " + (i + 1) + ": " + estomagoDoMacaco[i]);
                    }
                    break;

                case 3:
                    contador1--;
                    break;

                case 4:
                    System.out.println("\nTurno 1 Finalizado!");
                    break;

                default:
                    System.out.println("\nOpção Inválida!");
                    break;
            }
        } while (opcao != 4);

        do {
            opcao = menuJ2();
            switch (opcao) {
                case 1:
                    int numero = random.nextInt(6) + 1;
                    System.out.printf("Nesta rodada você pode alimentar %d vez(es)\n", numero);
                    for (int i = 0; i < numero; i++) {
                        System.out.print("Digite um alimento: ");
                        String alimento = sc.nextLine();
                        M2.adicionarComida(alimento);
                        contador2++;
                    }
                    break;

                case 2:
                    String[] estomagoDoMacaco = M2.getEstomago();
                    for (int i = 0; i < contador2; i++) {
                        System.out.println("Posição " + (i + 1) + ": " + estomagoDoMacaco[i]);
                    }
                    break;

                case 3:
                    contador2--;
                    break;

                case 4:
                    System.out.println("\nTurno 2 Finalizado!");
                    break;

                default:
                    System.out.println("\nOpção Inválida!");
                    break;
            }
        } while (opcao != 4);

        if (contador1 > contador2) {
            System.out.printf("\nO jogador %s Venceu!", nomeDoMacaco1);
        }
        else {
            System.out.printf("\nO jogador %s Venceu!", nomeDoMacaco2);
        }




    }
}
