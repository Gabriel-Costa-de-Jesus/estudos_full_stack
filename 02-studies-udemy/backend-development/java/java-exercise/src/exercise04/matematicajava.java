package exercise04;

public class matematicajava {
    public static void main(String[]args){

        double x = 4.0;
        double y = 9.0;
        double z = 15.0;

        double A, B, C;

        A = Math.sqrt(x);
        B = Math.sqrt(y);
        C = Math.sqrt(25.0);

        System.out.printf("Raiz quadrada de %.0f%n é %.0f%n", x, A);
        System.out.printf("Raiz quadrada de %.0f%n é %.0f%n", y, B);
        System.out.printf("Raiz quadrada de 25 é %.0f%n", C);

        A = Math.pow(x, z);
        B = Math.pow(x, 2.0);
        C = Math.pow(5.0, 2.0);


        System.out.printf("%.0f%n elevado a %.0f%n é %.0f%n", x, z, A);
        System.out.printf("%.0f%n elevado a 2 é %.0f%n", x, B);
        System.out.printf("5 elevado a 2 é %.0f%n", C);

        A = Math.abs(y);
        B = Math.abs(z);

        System.out.printf("Valor Absoluto de %.0f%n é %.0f%n ", y, A);
        System.out.printf("Valor Absoluto de %.0f%n é %.0f%n ", z, B);

    }
}
