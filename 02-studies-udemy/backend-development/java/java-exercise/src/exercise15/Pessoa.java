package exercise15;

public class Pessoa {
    private String nome;
    private double altura;

    public Pessoa(String nome, double altura){
        this.nome = nome;
        this.altura = altura;
    }
    public String getNome(){
        return nome;
    }
    public void SetNome(String nome){
        this.nome = nome;
    }
    public double getAltura(){
        return altura;
    }
    public void SetAltura(double altura){
        this.altura = altura;
    }
}
