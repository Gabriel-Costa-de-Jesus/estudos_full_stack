package interfaces;

public class Main {
    public static void main(String[]args){
        Cachorro c = new Cachorro();
        Gato g = new Gato();

        System.out.println("Gato");
        System.out.println(g.mia());
        System.out.println(g.caminha());

        System.out.println("\nCachorro");
        System.out.println(c.late());
        System.out.println(c.caminha());
    }
}
