package exercise01;

import java.util.Locale; // Importanto biblioteca para Locale

public class funcaoexterna {
    public static void imprimirexterno(){
        System.out.print("\nEu estou em outro arquivo no formato US!");
        double z = 10.90234;
        System.out.printf("\n%.2f%n", z);
        Locale.setDefault(Locale.US);

        // Imprimindo com print e printf
        System.out.print("\nO número: " + z + " É legal demais\n");
        System.out.printf("Resultado = %.2f metros%n", z);
    }
}