package interfaces.exercise02;

import java.util.Scanner;

public class Main {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int opcao;
        do {
            System.out.println("\nEscolha o Objeto Geométrico que deseja calcular");
            System.out.println("1- Circulo");
            System.out.println("2- Retângulo");
            System.out.println("3- Triângulo");
            System.out.println("4- Sair");
            System.out.print("Digite a sua opção: ");
            opcao = sc.nextInt();
            sc.nextLine();

            switch (opcao){
                case 1:
                    System.out.println("Digite o raio do Circulo: ");
                    double raio = sc.nextDouble();
                    Circulo c = new Circulo(raio);
                    System.out.printf("Área do Círculo: %.2f", c.calcularArea());
                    System.out.printf("%nPerimétro do Circulo: %.2f", c.calcularPerimetro());
                    break;

                case 2:
                    System.out.print("Digite a base: ");
                    double base = sc.nextDouble();

                    System.out.print("Digite a Altura: ");
                    double altura = sc.nextDouble();

                    Retangulo r = new Retangulo(base, altura);
                    System.out.printf("Área do Retângulo: %.2f", r.calcularArea());
                    System.out.printf("%nPerimétro do Reângulo: %.2f", r.calcularPerimetro());
                    break;
                case 3:
                    System.out.print("Digite o primeiro lado: ");
                    double l1 = sc.nextDouble();

                    System.out.print("Digite o segundo lado: ");
                    double l2 = sc.nextDouble();

                    System.out.print("Digite o terceiro lado: ");
                    double l3 = sc.nextDouble();

                    Triangulo t = new Triangulo(l1, l2, l3);
                    System.out.printf("Área do Triângulo: %.2f", t.calcularArea());
                    System.out.printf("%nPerimétro do Triângulo: %.2f", t.calcularPerimetro());
                    break;
                case 4:
                    System.out.println("Saindo do Sistema...");
                    break;
                default:
                    System.out.println("Opção Inválida!");
                    break;

            }
        } while (opcao != 4);
    }
}
