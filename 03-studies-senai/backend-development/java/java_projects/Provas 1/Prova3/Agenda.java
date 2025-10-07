package Prova3;

import java.util.Scanner;

public class Agenda {
    static Scanner sc = new Scanner(System.in);
    static Pessoa[] ps = new Pessoa[10];
    static int contador = 0;

    public void armazenaPessoa(String nome, int idade, double altura){
        Pessoa ps = new Pessoa(nome, idade, altura);
    }
    public void removePessoa(String nome){

    }

    public static int menu(){
        System.out.println("\nEscolha uma opção abaixo:");
        System.out.println("1 - Adicionar Pessoa");
        System.out.println("2 - Remover uma pessoa");
        System.out.println("3 - Buscar uma pessoa pelo nome");
        System.out.println("4 - Imprimir a agenda");
        System.out.println("5 - Imprimir os dados de contatos da agenda");
        System.out.println("6 - Saindo do Sistema");
        System.out.print("Escolha uma opção: ");
        int opcao = sc.nextInt();
        sc.nextLine();
        return opcao;
    }

    public static void armazenarPessoa(){
        if (contador >= ps.length){
            System.out.println("\nLimite de Pessoas Alcançadas!");
            return;
        }
        System.out.print("\nDigite o nome da Pessoa: ");
        String nome = sc.nextLine();
        System.out.print("\nDigite a idade da Pessoa: ");
        int idade = sc.nextInt();
        sc.nextLine();
        System.out.print("\nDigite a altura da Pessoa: ");
        double altura = sc.nextDouble();
        ps[contador] = new Pessoa(nome,idade,altura);

        System.out.printf("Pessoa %s Cadastrada com sucesso!\n", ps[contador].getNome());
        contador++;

    }
    public static void removePessoa(){
        if (contador == 0){
            System.out.println("Cadastre alguma Pessoa Primeiro!");
            return;
        }
        System.out.println("Pessoas cadastradas! ");
        for (int i =0; i < contador; i++){
            System.out.printf("\nNome: %s", ps[i].getNome());
        }

        System.out.println("\nEscolha uma pessoa para ser removida: ");
        String removep = sc.nextLine();

        for (int i =0; i < contador; i++){
            if (ps[i].getNome().equals(removep)){
                System.out.println("Pessoa Removida com Sucesso!");
                String nome = "";
                int idade = 0;
                double altura = 0;

                ps[i].setNome("");
                contador--;
                System.out.println(contador);
                break;
            }
        }

    }
    public static void buscaPessoa(){
        if (contador == 0){
            System.out.println("Cadastre alguma Pessoa Primeiro!");
            return;
        }

        System.out.println("Pessoas Cadastradas! ");
        for (int i =0; i < contador; i++){
            System.out.printf("\nNome: %s", ps[i].getNome());
        }

        System.out.print("\nEscolha uma pessoa para buscar: ");
        String buscap = sc.nextLine();

        for (int i =0; i < contador; i++){
            if (ps[i].getNome().equals(buscap)){
                System.out.println("\nPessoa Encontrada com Sucesso!");
                System.out.printf("\nNome da Pessoa: %s", ps[i].getNome());
                System.out.printf("\nIdade da Pessoa: %s", ps[i].getIdade());
                System.out.printf("\nAltura da Pessoa: %s \n", ps[i].getAltura());
            }
        }

    }
    public static void imprimeAgenda(){
        if (contador == 0){
            System.out.println("Cadastre alguma Pessoa Primeiro!");
            return;
        }

        for (int i =0; i < contador; i++){
            System.out.println("\nPessoas Cadastradas na Agenda!");
            System.out.printf("\nNome da Pessoa: %s", ps[i].getNome());
            System.out.printf("\nIdade da Pessoa: %s", ps[i].getIdade());
            System.out.printf("\nAltura da Pessoa: %s \n", ps[i].getAltura());

        }

    }
    public static void imprimePessoa(){
        if (contador == 0){
            System.out.println("Cadastre alguma Pessoa Primeiro!");
            return;
        }

        System.out.println("Pessoas Cadastradas! ");
        for (int i =0; i < contador; i++){
            System.out.printf("\nNome: %s", ps[i].getNome());
            System.out.printf("\nIndex: %d", i);
        }

        System.out.print("\nEscolha A posição do Index da pessoa para buscar: ");
        int imprimep = sc.nextInt();

        for (int i =0; i < contador; i++){
            if (imprimep == i){
                System.out.println("\nPessoa Encontrada com Sucesso!");
                System.out.printf("\nNome da Pessoa: %s", ps[i].getNome());
                System.out.printf("\nIdade da Pessoa: %s", ps[i].getIdade());
                System.out.printf("\nAltura da Pessoa: %s \n", ps[i].getAltura());
            }
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
        do {
            opcao = menu();
            switch (opcao){
                case 1:
                    armazenarPessoa();
                    break;
                case 2:
                    removePessoa();
                    break;
                case 3:
                    buscaPessoa();
                    break;
                case 4:
                    imprimeAgenda();
                    break;
                case 5:
                    imprimePessoa();
                    break;
                case 6:
                    sair();
                    break;
                default:
                    erro();
                    break;
            }
        } while(opcao != 6);
    }
}
