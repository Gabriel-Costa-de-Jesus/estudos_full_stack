package poo.exercise01;

import java.util.Scanner;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static Biblioteca bb = new Biblioteca();

    public static int menu(){
        System.out.println("\nEscolha Uma opção Abaixo:");
        System.out.println("1- Adicionar Livros");
        System.out.println("2- Adicionar Revista");
        System.out.println("3- Adicionar Jornal");
        System.out.println("4- Listar Materiais");
        System.out.println("5- Buscar Por título");
        System.out.println("6- Emprestar Material");
        System.out.println("7- Sair");
        System.out.print("Escolha sua opção: ");
        int opcao = sc.nextInt();
        sc.nextLine();
        return opcao;
    }
    public static void buscarPorTitulo(){
        System.out.print("\nDigite o nome da Obra que Deseja Encontrar: ");
        String titulo = sc.nextLine();

        bb.buscarPorTitulo(titulo);
    }
    public static void emprestarMaterial(){
        System.out.print("\nDigite o nome da Obra que Deseja Emprestar: ");
        String tituloEmprestar = sc.nextLine();
        MaterialBiblioteca material = bb.buscarPorTitulo(tituloEmprestar);
        bb.emprestarMaterial(material);
    }
    public static void sair(){
        System.out.println("Saindo do Sistema...");
    }
    public static void erro(){
        System.out.println("\nOpção Inválida! Tente Novamente");
    }
    public static void main(String[] args){
        int opcao;
        do {
            opcao = menu();


            switch (opcao){
                case 1:
                    bb.adicionarMaterial(1);
                    break;
                case 2:
                    bb.adicionarMaterial(2);
                    break;
                case 3:
                    bb.adicionarMaterial(3);
                    break;
                case 4:
                    bb.listarMaterias();
                    break;
                case 5:
                    buscarPorTitulo();
                    break;
                case 6:
                    emprestarMaterial();
                    break;
                case 7:
                    sair();
                    break;
                default:
                    erro();
                    break;
            }
        } while (opcao != 7);
    }
}
