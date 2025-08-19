package exercise01; //Aqui indica que está dentro do pacote exercise 01

public class Main { // Aqui coloca o nome da pasta
    public static void main(String[]args) { // Aqui é a função principal do programa, essa estrutura é obrigatória
        System.out.println("Olá mundo!");
        System.out.println("Bom dia!");
        imprimirClima();
        imprimirVariaveis();
        funcaoexterna.imprimirexterno();
        calculos();
    }

    public static void imprimirClima() { // Isso aqui é uma função normal
        System.out.println("\nO Clima de hoje está agradavél :)");
    }

    public static void imprimirVariaveis(){ //Declaração de Variáveis
        String nome = "Maria";
        int y = 32;
        double x = 10.35784;
        System.out.print("\nO número inteiro é: " + y);
        System.out.print("\nO número em Double(Real) é: " + x);
        System.out.printf("\nO número em Double(Real com 2 casas decimais) é: %.2f%n", x);
        System.out.printf("\nO nome dela é: %s e ela tem %d de idade", nome, y);
    }

    public static void calculos(){
        int n1 = 10;
        int n2 = 5;

        int soma = n1+n2;
        int sub = n1-n2;
        int mut = n1*n2;
        int div = n1/n2;

        System.out.println("Números somados, subtraídos, multiplicados e divididos");

        System.out.printf("\nSoma %d", soma);
        System.out.printf("\nSubtração %d", sub);
        System.out.printf("\nMultiplicação %d", mut);
        System.out.printf("\nDivisão %d", div);

    }

}