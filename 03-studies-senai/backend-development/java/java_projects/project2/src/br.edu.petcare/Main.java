package br.edu.petcare;
import model.*;
import service.Clinica;

import java.util.Scanner;
public class Main {
    static Scanner sc = new Scanner(System.in);
    static Funcionario f = new Funcionario();
    static Dono d = new Dono();
    static Animal a = new Animal();
    static Clinica c = new Clinica();

    public static int menu(){
        System.out.println("\nEscolha uma opção Abaixo:");
        System.out.println("1- Cadastrar Dono");
        System.out.println("2- Cadastrar Pet");
        System.out.println("3- Cadastrar Funcionário");
        System.out.println("4- Listar Funcionários");
        System.out.println("5- Listar Donos e Pets");
        System.out.println("6- Registrar Atendimento");
        System.out.println("7- Exibir Histórico de Atendimentos");
        System.out.println("0- Sair");
        System.out.print("Escolha sua opção: ");
        int opcao = sc.nextInt();
        sc.nextLine();
        return opcao;
    }
    private static void cadastrasrDono() {
        System.out.println("Opção Cadastrar Dono Selecionada! ");

        System.out.print("\nDigite o nome: ");
        String nome = sc.nextLine();

        System.out.print("\nDigite o telefone: ");
        String telefone = sc.nextLine();

        System.out.print("\nDigite o email: ");
        String email = sc.nextLine();

        System.out.print("\nDigite um nome de Usuário: ");
        String usuario = sc.nextLine();

        System.out.print("\nDigite uma senha: ");
        String senha = sc.nextLine();

        d = new Dono(nome, telefone, email, usuario, senha);
        c.cadastrarDono(d);
        System.out.printf("Pessoa %s Cadastrada com Sucesso!", nome);

    }

    private static void cadastrarPet() {
        System.out.println("Opção Cadastrar Dono Pet! ");

        System.out.print("\nDigite o nome: ");
        String nome = sc.nextLine();

        System.out.print("\nDigite a espécie: ");
        String especie = sc.nextLine();

        System.out.print("\nDigite a raça: ");
        String raca = sc.nextLine();

        System.out.print("\nDigite a idade do PET: ");
        int idade = sc.nextInt();
        sc.nextLine();

        System.out.print("\nDigite o peso: ");
        float peso = sc.nextFloat();

        System.out.print("\nDigite o nome do Dono para cadastrar o Pet: ");
        String buscarDono = sc.nextLine();
        boolean donoEncontrado = c.associarDono(buscarDono);

        if (donoEncontrado){
            System.out.println("Dono encontrado! Associação realizada.");
            String dono = buscarDono;
            a = new Animal(nome, especie, raca, dono, idade, peso);
            c.cadastrarAnimal(a);

        }
        else {
            System.out.println("Dono não encontrado. Falha na associação.");
            return;
        }
    }

    private static void cadastrarFuncionario() {
        System.out.print("\nDigite o nome: ");
        String nome = sc.nextLine();

        System.out.print("\nDigite o telefone: ");
        String telefone = sc.nextLine();

        System.out.print("\nDigite o email: ");
        String email = sc.nextLine();

        System.out.print("\nDigite um nome de Usuário: ");
        String usuario = sc.nextLine();

        System.out.print("\nDigite uma senha: ");
        String senha = sc.nextLine();

        System.out.print("\nDigite o Cargo: ");
        String cargo = sc.nextLine();

        System.out.print("\nDigite o salário: ");
        float salario = sc.nextFloat();
        sc.nextLine();

        f = new Funcionario(nome, telefone, email, usuario, senha, cargo, salario);
        c.cadastrarFuncionario(f);
        System.out.printf("Pessoa %s Cadastrada com Sucesso!", nome);

    }

    private static void listarFuncionarios() {
        if (c.getFuncionarios().isEmpty()){
            System.out.println("Lista Vazia! Cadastre algo primeiro! ");
            return;
        }

        System.out.println("Funcionários Cadastrados!");
        c.getFuncionarios();
    }

    private static void listarDonosEPet() {
        if (c.getDonos().isEmpty() && c.getAnimais().isEmpty()){
            System.out.println("Lista Vazia! Cadastre algo primeiro! ");
            return;
        }

        System.out.println("Donos e Pets Cadastrados!");
        c.getDonos();
        c.getAnimais();

    }

    private static void registrarAtendimento() {
        if (c.getDonos().isEmpty() && c.getAnimais().isEmpty()){
            System.out.println("Lista Vazia! Cadastre algo primeiro! ");
            return;
        }

        System.out.println("Qual Funcionário Registrou o atendimento? ");
        String funcionario = sc.nextLine();

        System.out.println("Qual o nome do Dono atendido? ");
        String dono = sc.nextLine();

        System.out.println("Qual pet foi atendido? ");
        String pet = sc.nextLine();

        System.out.println("Qual foi o serviço registrado?");
        String servico = sc.nextLine();

        System.out.println("Digite a data do atendimento (dd/mm/aaaa)");
        String data = sc.nextLine();

    }

    private static void exibirHistoricoAtendimento() {
        if (c.getAtendimentos().isEmpty()){
            System.out.println("Lista Vazia! Cadastre algo primeiro! ");
            return;
        }
        c.getAtendimento();
    }

    public static void erro(){
        System.out.println("Opção Inválida! Tente Novamente");
    }

    public static void sair(){
        System.out.println("Saindo do sistema...");
    }
    public static void main(String[]args){
        int opcao;
        do {
            opcao = menu();
            switch (opcao){
                case 0:
                    sair();
                    break;
                case 1:
                    cadastrasrDono();
                    break;
                case 2:
                    cadastrarPet();
                    break;
                case 3:
                    cadastrarFuncionario();
                    break;
                case 4:
                    listarFuncionarios();
                    break;
                case 5:
                    listarDonosEPet();
                    break;
                case 6:
                    registrarAtendimento();
                    break;
                case 7:
                    exibirHistoricoAtendimento();
                    break;
                default:
                    erro();
                    break;
            }
        } while (opcao != 0);
    }














}
