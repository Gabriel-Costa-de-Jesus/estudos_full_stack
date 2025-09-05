package exercise15;

import java.util.Scanner;

public class VetorArrayparte2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite quantas pessoas você deseja cadastrar: ");
        int posicoes = sc.nextInt();
        Pessoa[] pessoas = new Pessoa[posicoes];
        for (int i = 0; i < pessoas.length; i++) {
            sc.nextLine(); // Limpar a quebra de linha após usar int dps String
            System.out.print("\nDigite seu nome: ");
            String nome = sc.nextLine();

            System.out.print("Digite a sua altura: ");
            double altura = sc.nextDouble();

            pessoas[i] = new Pessoa(nome, altura);
        }
        for (int i = 0; i < posicoes; i++){
            System.out.printf("%nNome da Pessoa[%d]: %s", i+1, pessoas[i].getNome());
            System.out.printf("%nIdade da Pessoa[%d]: %.2f%n", i+1, pessoas[i].getAltura());

        }
    }
}
