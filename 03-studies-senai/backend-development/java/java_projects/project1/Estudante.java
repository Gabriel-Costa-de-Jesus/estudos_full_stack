package project1;

public class Estudante {
    private String nome;
    private int matricula;
    private double n1,n2,n3, media;

    public Estudante(){}
    public Estudante(String nome, int matricula, double n1, double n2, double n3){
        this.nome = nome;
        this.matricula = matricula;
        this.n1 = n1;
        this.n2 = n2;
        this.n3 = n3;
    }
    public String getNome(){
        return nome;
    }
    public int getMatricula(){
        return matricula;
    }
    public double getN1(){
        return n1;
    }
    public double getN2(){
        return n2;
    }
    public double getN3(){
        return n3;
    }

    public double calcularMedia(){
        return (n1+n2+n3)/3;
    }
}
