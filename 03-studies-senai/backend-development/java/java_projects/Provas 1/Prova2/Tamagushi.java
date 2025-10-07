package Questao3;

public class Tamagushi {
    private String nome;
    private double fome =100;
    private double tedio =100;
    private int idade;

    public Tamagushi(String nome, int idade){
        this.nome = nome;
        this.idade = idade;
    }
    public Tamagushi(){}

    public void brincar(double minutos){
        this.tedio -= minutos;
    }
    public void alimentar(double quantidade){
        this.fome -= quantidade;
    }
    public double getHumor(){
        return fome+tedio;
    }
    public double getFome(){
        return fome;
    }
    public double getTedio(){
        return tedio;
    }

}