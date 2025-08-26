package exercise01;

public class Pessoa {
    private String nome;
    private int idade;
    private double peso;
    private double altura;

    public void envelhecer(int idade){
        this.idade = idade;
    }
    public int getIdade(){
        return idade;
    }

    public void engordar(double peso){
        this.peso = peso;
    }
    public void emagrecer(double peso){
        this.peso = peso;
    }
    public double getPeso(){
        return peso;
    }

    public void crescer(double altura){
        this.altura = altura;
    }
    public double getAltura(){
        return altura;
    }
}
