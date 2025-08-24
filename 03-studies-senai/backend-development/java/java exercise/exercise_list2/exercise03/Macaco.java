package exercise03;

public class Macaco {
    String nome;
    String[] estomago = new String[3];

    public Macaco(String nome) {
        this.nome = nome;
    }

    public void comer(String alimento, int posicao) {
        if (posicao >= 0 && posicao < estomago.length) {
            estomago[posicao] = alimento;
            System.out.println(nome + " comeu " + alimento);
        }
    }

    public void verEstomago() {
        System.out.println("Estômago de " + nome + ":");
        for (int i = 0; i < estomago.length; i++) {
            System.out.println("  Posição " + i + ": " + estomago[i]);
        }
    }

    public void digerir() {
        for (int i = 0; i < estomago.length; i++) {
            estomago[i] = null;
        }
        System.out.println(nome + " digeriu tudo!");
    }
}
