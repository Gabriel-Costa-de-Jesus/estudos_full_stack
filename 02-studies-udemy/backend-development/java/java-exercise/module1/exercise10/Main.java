package exercise10;

import exercise10.Calculator;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Calculator calc = new Calculator();

        System.out.print("Digite o radius: ");
        double radius = sc.nextDouble();

        double c = calc.circuferencia(radius);
        double v = calc.volume(radius);

        System.out.printf("Área da Circuferencia: %.2f %n", c);
        System.out.printf("Área do volume: %.2f %n", v);
        System.out.printf("PI: %.2f %n", calc.PI);

        sc.close();
    }
}
