package model;

public class Animal {
        private String nome, especie, raca, dono;
        private int idade;
        private float peso;

    public Animal(String nome, String especie, String raca, String dono, int idade, float peso) {
        this.nome = nome;
        this.especie = especie;
        this.raca = raca;
        this.dono = dono;
        this.idade = idade;
        this.peso = peso;
    }
    public Animal(){}
}
