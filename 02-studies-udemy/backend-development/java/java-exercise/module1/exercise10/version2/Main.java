package exercise10.version2;

import exercise10.version2.Calculator;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //Calculator calc = new Calculator(); O static permite chamar a função de outra classe sem a necessidade de uma instancia

        System.out.print("Digite o radius: ");
        double radius = sc.nextDouble();

        double c = Calculator.circuferencia(radius);
        double v = Calculator.volume(radius);

        System.out.printf("Área da Circuferencia: %.2f %n", c);
        System.out.printf("Área do volume: %.2f %n", v);
        System.out.printf("PI: %.2f %n", Calculator.PI);

        sc.close();
    }
}
