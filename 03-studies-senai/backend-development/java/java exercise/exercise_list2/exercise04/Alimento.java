package exercise04;

public class Alimento {
    private String nome;
    private double kcal;

    public Alimento(String nome, double kcal) {
        this.nome = nome;
        this.kcal = kcal;
    }

    public String getNome(){
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public double getkcal() {
        return kcal;
    }
    public void setKcal(double kcal) {
        this.kcal = kcal;
    }
    public String toString() {
        return nome + " (" + kcal + " kcal)";
    }
}
