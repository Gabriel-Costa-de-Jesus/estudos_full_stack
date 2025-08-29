package exercise03;

import exercise03.Macaco;

public class Main {
    public static void main(String[] args) {
        Macaco m1 = new Macaco("Kong");
        Macaco m2 = new Macaco("George");

        m1.comer("Banana", 0);
        m1.verEstomago();

        m1.comer("Maçã", 1);
        m1.verEstomago();

        m1.comer("Uva", 2);
        m1.verEstomago();

        System.out.println();

        m2.comer("Manga", 0);
        m2.verEstomago();

        m2.comer("Abacaxi", 1);
        m2.verEstomago();

        m2.comer("Morango", 2);
        m2.verEstomago();

        System.out.println();

        m1.comer("Macaco George", 0); // força a comida ser "o outro macaco"
        m1.verEstomago();
    }
}
