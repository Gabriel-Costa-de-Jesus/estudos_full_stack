package exercise14;

import java.util.Scanner;

public class vetorArray {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Defina quantas possições no vetor você quer: ");

        int posicoes = sc.nextInt();

        double[] vetor = new double[posicoes];

        System.out.println("Digite 3 valores:");
        for (int i = 0; i < vetor.length; i++) { // Pegando a quantidade predefinida no vetor
            System.out.printf("%nPosição[%d]: ", i+1);
            vetor[i] = sc.nextDouble(); // Desse modo tou passando apenas um dado que é o valor para o vetor, se eu quisesse passar mais de um, como nome, valor, cep... seria de outra forma
        }


        double soma = 0.0;
        for (int i = 0; i < posicoes; i++) {
            soma += vetor[i];
        } // mesma coisa

        double media = soma/posicoes;

        System.out.printf("%nA média dos valores é: %.2f", media);

        sc.close();
    }
}
