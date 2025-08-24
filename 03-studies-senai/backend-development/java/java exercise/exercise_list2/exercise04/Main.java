package exercise04;

public class Main {
    public static void main(String[]args){
        Alimento[] estomago = new Alimento[3];

        estomago[0] = new Alimento("Maça", 52.0);
        estomago[1] = new Alimento("Arroz", 26.0);
        estomago[2] = new Alimento("Uva", 30.0);

        for(int i =0; i < estomago.length; i++) {
            System.out.printf("Alimento armazenado no vetor posição %d: %s%n", i, estomago[i]);

        }
    }
}
