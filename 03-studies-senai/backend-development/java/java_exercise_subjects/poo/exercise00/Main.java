package poo.exercise00;
import java.util.Scanner;

public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            Conta conta1 = new ContaCorrente("Gabriel", 1000);
            Conta conta2 = new ContaPoupanca("Maria", 500);

            int opcao;
            do {
                System.out.println("\n--- Menu ---");
                System.out.println("1. Depositar na Conta Corrente");
                System.out.println("2. Sacar da Conta Poupança");
                System.out.println("3. Mostrar Extratos");
                System.out.println("0. Sair");
                opcao = sc.nextInt();

                switch (opcao) {
                    case 1:
                        conta1.depositar(200);
                        break;
                    case 2:
                        conta2.sacar(100);
                        break;
                    case 3:
                        conta1.imprimirExtrato();
                        conta2.imprimirExtrato();
                        break;
                }
            } while (opcao != 0);

            sc.close();
        }
    }


