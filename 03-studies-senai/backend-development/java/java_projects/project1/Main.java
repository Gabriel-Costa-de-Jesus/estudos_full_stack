package project1;

import java.util.Scanner;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static Estudante[] estudante = new Estudante[3];
    static int contador = 0, contadorReprovados = 0, contadorAprovados =0, indiceMaior, indiceMenor;

    public static int menu(){
        System.out.println("\nEscolha uma opção abaixo: ");
        System.out.println("1 - Cadastrar estudante");
        System.out.println("2 - Exibir média dos estudantes");
        System.out.println("3 - Exibir classificação dos estudantes");
        System.out.println("4 - Relatório Final");
        System.out.println("5 - Sair");
        System.out.print("Digite a sua opção:");
        int opcao = sc.nextInt();
        sc.nextLine();
        return opcao;
    }
    public static void opcadastrarEstudante(){
        if (contador > estudante.length){
            System.out.println("Máximo de estudantes Atinjidos");
        }
        System.out.println("\nDigite o nome do estudante para ser cadastrado");
        String nome = sc.nextLine();
        System.out.println("Digite o código de matricula: ");
        int matricula = sc.nextInt();
        System.out.print("Digite a primeira nota: ");
        double n1 = sc.nextInt();
        System.out.print("Digite a segunda nota: ");
        double n2 = sc.nextInt();
        System.out.print("Digite a terceira nota: ");
        double n3 = sc.nextInt();
        estudante[contador] = new Estudante(nome, matricula, n1, n2, n3);
        contador++;

        System.out.println("\nEstudante cadastrado com sucesso!");

    }

    public static void opexibirMedias(){
        for (int i =0; i < contador; i++) {
            System.out.printf("\n3Estudante: %s", estudante[i].getNome());
            System.out.printf("\nNota da Primeira Unidade: %.2f",estudante[i].getN1());
            System.out.printf("\nNota da Segunda Unidade: %.2f",estudante[i].getN2());
            System.out.printf("\nNota da Terceira Unidade: %.2f",estudante[i].getN3());

            System.out.printf("\nMédia do estudante: %.2f%n",estudante[i].calcularMedia());
        }
    }
    public static void opclassificarAprovacao(){
         contadorReprovados = 0; contadorAprovados =0;
        for (int i =0; i < contador; i++) {
            System.out.printf("\nEstudante: %s", estudante[i].getNome());
            System.out.printf("\nMédia dos estudante: %.2f",estudante[i].calcularMedia());
            if (estudante[i].calcularMedia() > 7){
                System.out.print("\nAprovado\n");
                contadorAprovados++;

            }
            else {
                System.out.print("\nReprovado\n");
                contadorReprovados++;
            }
        }
    }
    public static void opgerarRelatorio(){
        contadorReprovados = 0; contadorAprovados =0;
        for (int i =0; i < contador; i++) {
            if (estudante[i].calcularMedia() > 7){
                contadorAprovados++;
            }
            else {
                contadorReprovados++;
            }
        }

        double contadormaior=0, contadormenor = 99;
        for (int i =0; i < contador; i++){
            if (estudante[i].calcularMedia() > contadormaior){
                indiceMaior = i;
                contadormaior= estudante[i].calcularMedia();
            }
            if (estudante[i].calcularMedia() < contadormenor){
                indiceMenor=i;
                contadormenor= estudante[i].calcularMedia();
            }
        }
        System.out.printf("\nQuantidade de alunos aprovados: %d", contadorAprovados);
        System.out.printf("\nQuantidade de alunos Reprovados: %d", contadorReprovados);
        System.out.printf("\nEstudante com a maior média: %s", estudante[indiceMaior].getNome());
        System.out.printf("\nEstudante com a menor média: %s%n", estudante[indiceMenor].getNome());
    }
    public static void sair(){
        System.out.println("\nSaindo do Sistema...");
    }
    public static void erro(){
        System.out.println("\nOpção Inválida, Tente Novamente!");
    }
    public static void main(String[]args){
        int opcao;
        do{
            opcao = menu();
            switch (opcao) {
                case 1:
                    opcadastrarEstudante();
                    break;
                case 2:
                    opexibirMedias();
                    break;
                case 3:
                    opclassificarAprovacao();
                    break;
                case 4:
                    opgerarRelatorio();
                    break;
                case 5:
                    sair();
                    break;
                default:
                    erro();
                    break;
            }
        } while (opcao != 5);

    }
}
