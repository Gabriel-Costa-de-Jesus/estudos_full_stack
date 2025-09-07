package exercise07;

public class operadorternario {
    public static void main(String[]args) {
        double produto1 = 34.5;
        double produto2 = 50.5;

        System.out.println((produto1 < 50.0) ? "Produto 1 Sem Desconto" : "Produto 1 Com Desconto");

        String desconto = (produto2 > 30) ? "Produto 2 com desconto" : "Produto 2 sem desconto";

        System.out.print(desconto);


    }
}
